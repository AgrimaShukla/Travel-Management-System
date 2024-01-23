''' This module keeps all the queries for database'''
class InitializeDatabase:
    CREATE_DATABASE = 'CREATE DATABASE IF NOT EXISTS {}'
    USE_DATABASE = 'USE {}'

class Query:
    '''This class contains all the queries'''
    
    # CREDENTIALS TABLE
    CREATE_CREDENTIALS = ''' CREATE TABLE IF NOT EXISTS credentials(
            user_id VARCHAR(20) PRIMARY KEY,
            username VARCHAR(12) UNIQUE,
            password VARCHAR(100),
            role VARCHAR(8)  
        )
    '''
    INSERT_CREDENTIALS = '''INSERT INTO credentials(
                user_id, username, password, role) 
                VALUES
                (%s, %s ,%s, %s)
    '''
    SELECT_CREDENTIALS_USERNAME = 'SELECT user_id, password, role FROM credentials WHERE username = %s'

    SELECT_CREDENTIALS_PASSWORD = 'SELECT role, user_id FROM credentials WHERE username = %s AND password = %s'

    # CUSTOMER TABLE
    CREATE_CUSTOMER = ''' CREATE TABLE IF NOT EXISTS customer(
                customer_id VARCHAR(20) PRIMARY KEY,
                name  VARCHAR(20),
                mobile_number  VARCHAR(10) UNIQUE,
                gender VARCHAR(10),
                age VARCHAR (3),
                email  VARCHAR(15) UNIQUE,
                FOREIGN KEY (customer_id) REFERENCES credentials(user_id) ON DELETE CASCADE
        )
    '''
    INSERT_USER = 'INSERT INTO customer VALUES(%s, %s, %s, %s, %s, %s)'

    SELECT_CUSTOMER = 'SELECT name, mobile_number, gender, age, email from customer WHERE customer_id = %s'
   
    UPDATE_CUSTOMER = 'UPDATE customer SET {} = %s WHERE customer_id = %s'

    # ADMIN TABLE
    CREATE_ADMIN = ''' CREATE TABLE IF NOT EXISTS admin(
                admin_id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(20),
                mobile_number VARCHAR(10),
                gender VARCHAR(10),
                age INTEGER,
                email VARCHAR(40) UNIQUE,
                FOREIGN KEY (admin_id) REFERENCES credentials(user_id) ON DELETE CASCADE
    )
    ''' 

    INSERT_ADMIN = '''INSERT INTO admin(
                    admin_id,
                    name, 
                    mobile_number,
                    gender,
                    age,
                    email
    ) VALUES (%s, %s, %s, %s, %d, %s)
    '''

    # PACKAGE TABLE 
    CREATE_PACKAGE = ''' CREATE TABLE IF NOT EXISTS package(
                package_id VARCHAR(20) PRIMARY KEY,
                package_name VARCHAR(20),
                duration VARCHAR(20),
                category VARCHAR(20),
                price VARCHAR(10),
                status VARCHAR(20)
    )
    '''

    CHANGE_STATUS_QUERY = 'UPDATE package SET status = %s WHERE package_id = %s'
    
    INSERT_PACKAGE_QUERY = '''INSERT INTO package VALUES(%s, %s, %s, %s, %s, %s)'''

    SELECT_ADMIN = 'SELECT * FROM credentials WHERE role = %s'
    
    SELECT_PRICE = 'SELECT package_id, price, duration FROM package WHERE package_name = %s AND category = %s AND duration = %s AND status = %s'

    CHECK_PACKAGE_QUERY = 'SELECT * FROM package WHERE package_id = %s'

    SELECT_PACKAGE_QUERY = 'SELECT * FROM package WHERE status != %s'

    SELECT_PACKAGE = 'SELECT * FROM package'

    UPDATE_PACKAGE_QUERY = 'UPDATE package SET {} = %s WHERE package_id = %s'

    # ITINERARY TABLE
    CREATE_ITINERARY = ''' CREATE TABLE IF NOT EXISTS itinerary(
                itinerary_id VARCHAR(20) PRIMARY KEY,
                package_id VARCHAR(20),
                day INTEGER,
                city VARCHAR(20),
                description VARCHAR(20),
                FOREIGN KEY (package_id) REFERENCES package(package_id) ON DELETE CASCADE
    )
    '''

    UPDATE_ITINERARY_QUERY = 'UPDATE itinerary SET {} = %s WHERE itinerary_id = %s'

    INSERT_ITINERARY_QUERY = '''INSERT INTO itinerary(
                itinerary_id,
                package_id,
                day,
                city,
                description
    ) VALUES (%s, %s, %s, %s, %s)
    '''

    SELECT_ITINERARY = '''SELECT itinerary.day, itinerary.city, itinerary.desc
                FROM itinerary
                INNER JOIN package ON package.package_id = itinerary.package_id
                WHERE package.package_name = %s
                AND package.category = %s
                AND package.duration = %s
                AND package.status = %s
    '''

    SHOW_ITINERARY_QUERY = 'SELECT * FROM itinerary'

    CHECK_ITINERARY_QUERY = 'SELECT * FROM itinerary WHERE itinerary_id = %s'

    # BOOKING TABLE
    CREATE_BOOKING = ''' CREATE TABLE IF NOT EXISTS booking(
                booking_id VARCHAR(20) PRIMARY KEY,
                name VARCHAR(20),
                mobile_number VARCHAR(20),
                start_date VARCHAR(20),
                end_date VARCHAR(20),
                no_of_people INTEGER,
                email VARCHAR(20),
                booking_date VARCHAR(20)
    )
    '''
    INSERT_BOOKING = ''' INSERT INTO booking
                VALUES
                (%s, %s, %s, %s, %s, %d, %s, %s)
    '''

    # BOOKING PACKAGE TABLE
    CREATE_BOOKING_PACKAGE = '''CREATE TABLE IF NOT EXISTS booking_package(
                package_id VARCHAR(20),
                customer_id VARCHAR(20),
                booking_id VARCHAR(20),
                price INTEGER,
                trip_status VARCHAR(20),
                FOREIGN KEY (package_id) REFERENCES PACKAGE (package_id),
                FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id),
                FOREIGN KEY (booking_id) REFERENCES BOOKING(booking_id),
                PRIMARY KEY (package_id, customer_id, booking_id)
    )
    '''

    INSERT_BOOKING_PACKAGE = ''' INSERT INTO booking_package VALUES (%s, %s, %s, %d, %s)'''

    UPDATE_BOOKING = 'UPDATE BOOKING_PACKAGE SET trip_status = %s WHERE booking_id = %s'


    SELECT_BOOKING = '''SELECT booking.booking_id, booking.name, booking.mobile_number, booking.start_date, booking.end_date, 
                    booking.no_of_people, booking.email, booking.booking_date, booking_package.trip_status 
                    FROM booking
                    INNER JOIN booking_package ON booking_package.booking_id = booking.booking_id
                    WHERE booking_package.customer_id = %s
                    '''

    BOOKING_NOT_CANCELLED = '''SELECT booking.booking_id, booking.name, booking.mobile_number, booking.start_date, booking.end_date, 
                    booking.no_of_people, booking.email, booking.booking_date, booking_package.trip_status 
                    FROM booking
                    INNER JOIN booking_package ON booking_package.booking_id = booking.booking_id
                    WHERE booking_package.customer_id = %s AND booking_package.trip_status = %s AND booking.start_date >= %s
                    '''
    PACKAGE_FROM_BOOKING = '''SELECT day, city, desc FROM itinerary WHERE package_id IN (SELECT package_id FROM booking_package WHERE booking_id = %s)'''

    SELECT_FOR_REVIEW = '''SELECT booking.booking_id, booking_package.package_id, booking.start_date, booking.end_date 
                    FROM booking
                    INNER JOIN booking_package ON booking.booking_id = booking_package.booking_id 
                    WHERE booking_package.customer_id = %s AND booking_package.trip_status = %s AND booking.end_date <= %s'''

    SELECT_PACKAGE_REVIEW = 'SELECT package_id FROM booking_package WHERE booking_id = %s'

    # REVIEW TABLE
    CREATE_REVIEW = ''' CREATE TABLE IF NOT EXISTS review(
                    review_id VARCHAR(20) PRIMARY KEY,
                    booking_id VARCHAR(20),
                    package_id VARCHAR(20),
                    name VARCHAR(20),
                    comment VARCHAR(20),
                    date VARCHAR(20),
                    FOREIGN KEY (booking_id) REFERENCES booking(booking_id) ON DELETE CASCADE,
                    FOREIGN KEY (package_id) REFERENCES package(package_id) ON DELETE CASCADE
    )
'''

    INSERT_REVIEW = '''INSERT INTO review
                    VALUES
                    (%s, %s, %s, %s, %s, %s)
    '''

    SELECT_REVIEW = 'SELECT name, comment, date FROM review WHERE package_id = %s'

class DatabaseConfig:
    '''Database path'''

    DB_PATH = 'travelmanagementsystem.db'
    
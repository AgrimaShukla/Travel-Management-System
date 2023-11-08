''' This module keeps all the queries for database'''

class Query:
    '''This class contains all the queries'''
    
    # CREDENTIALS TABLE
    CREATE_CREDENTIALS = ''' CREATE TABLE IF NOT EXISTS credentials(
            user_id TEXT PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT  
        )
    '''
    INSERT_CREDENTIALS = '''INSERT INTO credentials(
                user_id, username, password, role) 
                VALUES
                (?, ? ,?, ?)
    '''
    SELECT_CREDENTIALS_USERNAME = 'SELECT password FROM credentials WHERE username = ?'

    SELECT_CREDENTIALS_PASSWORD = 'SELECT role, user_id FROM credentials WHERE username = ? AND password = ?'

    # CUSTOMER TABLE
    CREATE_CUSTOMER = ''' CREATE TABLE IF NOT EXISTS customer(
                customer_id TEXT PRIMARY KEY,
                name TEXT,
                mobile_number INTEGER UNIQUE,
                gender TEXT,
                age INTEGER,
                email TEXT UNIQUE,
                FOREIGN KEY (customer_id) REFERENCES credentials(user_id) ON DELETE CASCADE
        )
    '''
    INSERT_CUSTOMER = '''INSERT INTO customer(
                customer_id, name, mobile_number, gender, age, email) 
                VALUES
                (?, ?, ?, ?, ?, ?)
    '''

    # ADMIN TABLE
    CREATE_ADMIN = ''' CREATE TABLE IF NOT EXISTS admin(
                admin_id TEXT PRIMARY KEY,
                name TEXT,
                mobile_number INTEGER,
                gender TEXT,
                age INTEGER,
                email TEXT UNIQUE,
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
    ) VALUES (?, ?, ?, ?, ?, ?)
    '''

    # PACKAGE TABLE 
    CREATE_PACKAGE = ''' CREATE TABLE IF NOT EXISTS package(
                package_id TEXT PRIMARY KEY,
                package_name TEXT,
                duration TEXT,
                category TEXT,
                price INTEGER,
                lmt INTEGER,
                status TEXT
    )
    '''
    INSERT_PACKAGE_QUERY = '''INSERT INTO package VALUES(?, ?, ?, ?, ?, ?, ?)'''

    SELECT_ADMIN = 'SELECT * FROM credentials WHERE role = ?'
    
    SELECT_PRICE = 'SELECT price FROM package WHERE package_name = ? AND category = ? AND duration = ? AND status = ?'

    CHECK_PACKAGE_QUERY = 'SELECT * FROM package WHERE package_id = ?'

    SELECT_PACKAGE_QUERY = 'SELECT * FROM package WHERE status != ?'

    SELECT_PACKAGE = 'SELECT * FROM package'

    CHANGE_STATUS_QUERY = 'UPDATE package SET status = ? WHERE package_id = ?'

    UPDATE_PACKAGE_QUERY = 'UPDATE package SET {} = ? WHERE package_id = ?'

    # ITINERARY TABLE
    CREATE_ITINERARY = ''' CREATE TABLE IF NOT EXISTS itinerary(
                itinerary_id TEXT PRIMARY KEY,
                package_id TEXT,
                day INTEGER,
                city TEXT,
                desc TEXT,
                FOREIGN KEY (package_id) REFERENCES package(package_id) ON DELETE CASCADE
    )
    '''

    UPDATE_ITINERARY_QUERY = 'UPDATE itinerary SET {} = ? WHERE itinerary_id = ?'

    INSERT_ITINERARY_QUERY = '''INSERT INTO itinerary(
                itinerary_id,
                package_id,
                day,
                city,
                desc
    ) VALUES (?, ?, ?, ?, ?)
    '''

    SELECT_ITINERARY = '''SELECT package.package_id, package.duration, itinerary.day, itinerary.city, itinerary.desc
                FROM package
                INNER JOIN itinerary ON package.package_id = itinerary.package_id
                WHERE package.package_name = ?
                AND package.category = ?
                AND package.duration = ?
                AND package.status = ?
                AND package.lmt > 0

    '''

    SHOW_ITINERARY_QUERY = 'SELECT * FROM itinerary'

    CHECK_ITINERARY_QUERY = 'SELECT * FROM itinerary WHERE itinerary_id = ?'

    # BOOKING TABLE
    CREATE_BOOKING = ''' CREATE TABLE IF NOT EXISTS booking(
                booking_id TEXT PRIMARY KEY,
                name VARCHAR,
                mobile_number INTEGER,
                start_date TEXT,
                end_date TEXT,
                no_of_people INTEGER,
                email TEXT,
                booking_date TEXT
    )
    '''
    INSERT_BOOKING = ''' INSERT INTO booking
                VALUES
                (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # BOOKING PACKAGE TABLE
    CREATE_BOOKING_PACKAGE = '''CREATE TABLE IF NOT EXISTS booking_package(
                package_id TEXT,
                customer_id TEXT,
                booking_id TEXT,
                price INTEGER,
                trip_status TEXT,
                FOREIGN KEY (package_id) REFERENCES PACKAGE (package_id),
                FOREIGN KEY (customer_id) REFERENCES CUSTOMER (customer_id),
                FOREIGN KEY (booking_id) REFERENCES BOOKING(booking_id)
    )
    '''

    INSERT_BOOKING_PACKAGE = ''' INSERT INTO booking_package VALUES (?, ?, ?, ?, ?)'''

    UPDATE_BOOKING = 'UPDATE BOOKING_PACKAGE SET trip_status = ? WHERE booking_id = ?'

    ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON"

    SELECT_BOOKING = '''SELECT booking.booking_id, booking.name, booking.mobile_number, booking.start_date, booking.end_date, 
                    booking.no_of_people, booking.email, booking.booking_date, booking_package.trip_status 
                    FROM booking
                    INNER JOIN booking_package ON booking_package.booking_id = booking.booking_id
                    WHERE booking_package.customer_id = ?
                    '''

    BOOKING_NOT_CANCELLED = '''SELECT booking.booking_id, booking.name, booking.mobile_number, booking.start_date, booking.end_date, 
                    booking.no_of_people, booking.email, booking.booking_date, booking_package.trip_status 
                    FROM booking
                    INNER JOIN booking_package ON booking_package.booking_id = booking.booking_id
                    WHERE booking_package.customer_id = ? AND booking_package.trip_status = ?
                    '''
    PACKAGE_FROM_BOOKING = '''SELECT day, city, desc FROM itinerary WHERE package_id IN (SELECT package_id FROM booking_package WHERE booking_id = ?)'''

class DatabaseConfig:
    '''Database path'''
    
    DB_PATH = 'src\\database\\travelmanagementsystem.db'
    
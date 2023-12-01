'''This module keeps all the prompts'''

class PrintPrompts:
      '''One liner and multi liner prompts for displaying to user'''

      ADDED = 'ADDED'

      ADMIN_MENU = '''
            SELECT ANY OPTION:
            1) ADD PACKAGE
            2) DEACTIVATE PACKAGE
            3) ACTIVATE PACKAGE
            4) SHOW PACKAGE
            5) UPDATE PACKAGE
            6) UPDATE ITINERARY TABLE
            7) EXIT
      '''

      ATTEMPTS = "Attempts exhausted"
      
      BOOKING = '''
            SELECT ANY OPTION:
            1) PROCEED WITH BOOKING
            2) SHOW REVIEWS
            3) EXIT
      '''

      BOOKING_ID = "BOOKING ID {} DOES NOT EXIST. ENTER AGAIN"
      
      BOOKED_SUCCESSFULLY = "Booked successfully!\nPrice: {}\nBooking id: {}"

      CANCELLED = 'CANCELLED'

      CATEGORY_PROMPT = '''
            SELCT ANY OPTION:
            1) LUXURY
            2) MID-RANGE
            3) BUDGET
            4) EXIT

            Enter any option
      '''

      CHANGED = 'STATUS CHANGED'

      CUSTOMER_DETAILS = '''
            SELECT ANY OPTION:
            1) NAME
            2) MOBILE NUMBER
            3) GENDER
            4) AGE
            5) EMAIL
            6) EXIT
      '''

      DATE = " ENTER A DATE (YYYY-MM-DD)"

      DAY_PROMPT= '''
            SELECT ANY OPTION:
            1) 2 days 1 night
            2) 3 days 2 night
            3) 4 days 3 night
            4) EXIT

            Enter any option
      '''

      DESTINATION_PROMPT = '''
            SELECT ANY OPTION:
            1) Beaches
            2) Monuments
            3) Hill stations
            4) Religious
            5) Wild life
            6) Exit

            Enter any option
      '''

      ENTRY = '''
            SELECT ONE OPTION:
            1) REGISTER
            2) LOGIN
      '''
      INVALID_BOOKING = '''
            INVALID BOOKING ID.
            ENTER AGAIN.
      '''
      INVALID_CREDENTIALS = '''INVALID USERNAME OR PASSWORD! ENTER AGAIN'''
      
      INVALID_DATE_FORMAT = "INVALID DATE FORMAT. PLEASE USE 'YYYY-MM-DD'."

      INVALID_DATE = "INVVALID DATE"

      INVALID_PROMPT = '''
      INVALID OPTION
      ENTER AGAIN.
      '''

      ITINERARY_MENU = '''
            SELECT ANY OPTION:
            1) ADD ITINERARY
            2) SHOW ITINERARY
            3) UPDATE ITINERARY
            4) EXIT
      '''

      LOGIN_ATTEMPTS = "YOU HAVE 3 LOGIN ATTEMPTS"

      NAME = 'WELCOME TO MAHARASHTRA TOURS AND TRAVELS'

      NO_PACKAGE = 'NO PACKAGE FOUND WITH ID {}'

      NO_ITINERARY = 'NO ITINERARY FOUND WITH ID {}'
      
      NO_ITINERARY_FOUND = 'NO ITINERARY FOUND'

      NO_PACKAGE_FOUND = "NO PACKAGE FOUND"

      NO_BOOKINGS = "NO BOOKINGS"

      PACKAGE_NOT_FOUND = 'PACKAGE DOES NOT EXIST. FIRST ADD PACKAGE TO ADD AN ITINERARY.'

      PASSWORD = '''
            Password should contain:
            1) Minimum 8 characters in length.
            2) At least one uppercase English letter. 
            3) At least one lowercase English letter. 
            4) At least one digit. 
            5) At least one special character.      '''

      PRICE = "Price: {}"

      REVIEW = 'REVIEW ADDED'
      
      SUCCESFULLY = "Successfully registered"

      
      UPDATE_PACKAGE = '''
            SELECT ANY OPTION:
            1) PACKAGE NAME
            2) DURATION
            3) CATEGORY
            4) PRICE
      '''

      UPDATE_ITINERARY = '''
            SELECT ANY OPTION:
            1) DAY
            2) CITY
            3) DESCRIPTION
      '''
      UPDATED = "UPDATED"

      UNEXPECTED_ISSUE = "UNEXPECTED ISSUE OCCURRED. PLEASE TRY AGAIN LATER."

      USER_EXISTS = "USER ALREADY EXISTS"

      USER_MENU = '''
            SELECT ANY OPTION:
            1) BOOK PACKAGE
            2) CANCEL BOOKING
            3) VIEW BOOKINGS
            4) SHOW MY DETAILS
            5) UPDATE MY DETAILS
            6) ADD REVIEW
            7) EXIT
      '''

class InputPrompts:
      '''All the prompts used when taking input'''
      INPUT = "Enter {}: "
      
      EMAIL = '''ENTER EMAIL ID: '''

      ENTER = "ENTER: "

      ENTER_DETAIL = 'ENTER {}: '

      ITINERARY_ID = "ITINERARY ID: "

      PACKAGE_ID = "PACKAGE ID: "

      DURATION = "Enter duration (Eg - 3 days 2 nights): "

      EMAIL = "Enter email (Eg: - abc@gmail.com): "

      GENDER = "Enter gender (Eg - male|female|other): "

      NO_OF_PEOPLE = "Enter number of people (10 or less): "

      STATUS = "Enter status (active/inactive): "

class LoggingPrompt:
      '''Prompts for logging'''

      NO_DATA = "NO DATA FOUND"

      ADDED_PACKAGE = "ADDED PACKAGE"

      NO_PACKAGE = "NO PACKAGE FOUND"

      BOOKED = "BOOKED SUCCESSFULLY"

      REGISTERED = 'USER REGISTERED'

class TabulateHeader:
      '''Prompts for Tabulate'''

      AGE ="AGE"
      
      BOOKING_DATE = "BOOKING DATE"

      BOOKING_ID = "BOOKING ID"

      CATEGORY = "CATEGORY"

      CITY = "CITY"

      COMMENT = 'COMMENT'

      DATE = 'DATE'
      
      DAY = "DAY"

      DESC = "DESCRIPTION"

      DURATION = "DURATION"

      EMAIL = "EMAIL"

      END_DATE = "END DATE"

      GENDER = "GENDER"

      ITINERARY_ID = "ITINERARY ID"

      LIMIT = "LIMIT"

      PACKAGE_ID = "PACKAGE ID"

      PACKAGE_NAME = "PACKAGE NAME"

      MOBILE_NUMBER = "MOBILE NUMBER"

      NAME = "NAME"

      NO_OF_PEOPLE = "NO OF PEOPLE"

      PRICE = "PRICE"

      START_DATE = "START DATE"

      STATUS = "STATUS" 

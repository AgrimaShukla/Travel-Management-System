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

      BOOKING = '''
            SELECT ANY OPTION:
            1) PROCEED WITH BOOKING
            2) EXIT
      '''

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
      PASSWORD SHOULD BE BETWEEN LENGTH 5 AND 20
      '''

      PRICE = "Price: {}"

      SUCCESFULLY = "Successfully registered"

      UPDATE_PACKAGE = '''
            SELECT ANY OPTION:
            1) UPDATE PACKAGE NAME
            2) UPDATE DURATION
            3) UPDATE CATEGORY
            4) UPDATE PRICE
            5) UPDATE LIMIT
      '''

      UPDATE_ITINERARY = '''
            SELECT ANY OPTION:
            1) UPDATE DAY
            2) UPDATE CITY
            3) UPDATE DESCRIPTION
      '''
      UPDATED = "UPDATED"

      UNEXPECTED_ISSUE = "UNEXPECTED ISSUE OCCURRED. PLEASE TRY AGAIN LATER."

      USER_EXISTS = "USER ALREADY EXISTS"

      USER_MENU = '''
            SELECT ANY OPTION:
            1) BOOK PACKAGE
            2) CANCEL BOOKING
            3) VIEW BOOKINGS
            4) EXIT
      '''

class InputPrompts:
      '''All the prompts used when taking input'''
      INPUT = "Enter {}: "

      ENTER = "ENTER: "

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

class TabulateHeader:
      '''Prompts for Tabulate'''

      BOOKING_DATE = "BOOKING DATE"

      CATEGORY = "CATEGORY"

      CITY = "CITY"

      DAY = "DAY"

      DESC = "DESCRIPTION"

      DURATION = "DURATION"

      EMAIL = "EMAIL"

      END_DATE = "END DATE"

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

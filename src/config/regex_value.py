'''This module keeps all the regular expressions'''

class RegularExp:
    """Regular expressions for validation"""

    AGE = '[1-9][0-9]|10[1-9]'
    DURATION = '^([2-5]\sdays\s[1-4]\snights)$'
    EMAIL = '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
    GENDER = 'male|female|other'
    MOBILE_NUMBER = '[6-9][0-9]{9}'
    NAME = '^([A-Za-z]{2,25}\s*)+'
    NUMBER_VALUE = '^[0-9]+'
    PASSWORD = '^.{5,20}$'
    PERSON = '^(10|[1-9])$'
    STATUS = 'active|inactive'
    STRING_VALUE = '^([A-Za-z]{2,25}\s*)+'
    USERNAME = '^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=])[A-Za-z\d@#$%^&+=]+$'
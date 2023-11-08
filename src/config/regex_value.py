'''This module keeps all the regular expressions'''

class RegularExp:
    '''Regular expressions for validation'''

    AGE = r'[1-9][0-9]|10[1-9]'
    DURATION = r'^([2-5]\sdays\s[1-4]\snights)$'
    EMAIL = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
    GENDER = r'male|female|other'
    MOBILE_NUMBER = r'[6-9][0-9]{9}'
    NAME = r'^([A-Za-z]{2,25}\s*)+'
    NUMBER_VALUE = r'^[0-9]+'
    PASSWORD = r'^.{5,20}$'
    PERSON = r'^(10|[1-9])$'
    STATUS = r'active|inactive'
    STRING_VALUE = r'^([A-Za-z]{2,25}\s*)+'
    USERNAME =  r'[A-Za-z0-9._]{2,30}'
    UUID = r'^[A-Za-z0-9_]+$'
    
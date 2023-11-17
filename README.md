TRAVEL MANAGEMENT SYSTEM

The Tours and travels project is a console project which is built to optimize the booking facility offered to customers. It offers functionalities to simplify booking of the packages offered by the site. Various functionalities are implemented to provide user-friendly access. This project is built in python and sqlite. 

Modules:
1)	Admin module:
    •	One admin for the system
    •	Authenticated when providing username and password.
    •	It is responsible for handling package and itinerary module.
    •	Perform many operations like adding and updating the modules.
2)	Customer module
    •	Multiple customers for the system.
    •	Register themselves.
    •	Authenticated when providing username and password.
    •	They can see packages offered by the system by providing preferences.
    •	Book packages after viewing packages.
    •	Cancel packages booked in the past.
3)	Package module
    •	Package details added by admin.
    •	Viewed by user.
    •	Input validation using regex when added by admin.
    •	Can be updated by admin.
4)	Itinerary module
    •	Itinerary details added by admin.
    •	Viewed by user.
    •	Input validation using regex when added by admin.
    •	Can be updated by admin.
5)	Booking module
    •	Customer can book packages by providing personal information and information needed for booking.
    •	Booking can be viewed by customer.
    •	Can be cancelled by customer.


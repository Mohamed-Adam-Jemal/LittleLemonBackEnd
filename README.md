# LittleLemonBackEnd

HI!

Please adjust the database config in the setting.py file with you username and password to make the app works correctly.

The trailing slash in the end of the apis endpoints is necessary.. Please don't remove it to let the app apis work properly.


Check this api endpoint for the static html content
http://127.0.0.1:8000/restaurant/


APIs

Create new user: POST http://127.0.0.1:8000/auth/users/  

generate user token: POST http://127.0.0.1:8000/auth/token/login


Use this token to perform the http method operations with Insomnia or Postman or any other app

40591bc4f4f8df55bbcf6e84f5f0e945c85a6018

Add menu item: POST GET http://127.0.0.1:8000/restaurant/menu-items/  (Add the necessary field in the post request body)
Display Menu items: GET http://127.0.0.1:8000/restaurant/menu-items/ 
Display Menu single items (id=1): GET http://127.0.0.1:8000/restaurant/menu-items/1/
Display Reservations: GET http://127.0.0.1:8000/restaurant/booking/tables/
Display single Reservation (id=1): GET http://127.0.0.1:8000/restaurant/booking/tables/1/


You can also make the other http methods put, patch and delete with the same concept.. Just be careful when adding form labels.
You can also make http requests without token and chech for the permissions.




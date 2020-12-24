# Authentication and Authorization..

Basically what goes on in the web9security) has to do with these two, Authentication involves validating to see user details matches with what's created in the DB during a Signup process or rather a register process, Basic Stuff..

Inrespective of the fact that the django app now moves from one lower level to another level(a higher one per-say) DJANGO is still and always will be responsible for authentication.

DRF can/might play a Role, but that will be in terms of Serializing data and helping in the Passage flow of data(The data cycle , entering and leaving).. now even tho thats the role of it(DRF) it also adds another effective advantage to us by ensuring the data leaving and entering our application is secured and as to how django wants it, love DRF!!!!.

## Authentication

like i said earlier, django simply handles the authentication, so thats a django stuff common to us all django devs.


## Authorization

now basically before this, how is everything going to work out for us??

This is a story representation of it.

--- I signup in the application, django checks to see if data is cleaned, it then adds me to the DB and then issue a Token for me to use as to always confirm my identity with it.

---- Probably, i'm redirected to login again, i enter my credentials and django authenticates and finds my okay, it then creates a token again for me ..

---- Now as an authenticated user trying to make a request to the Server, i will need [#AUTHORIZATION] to do stuff like creating a tweet, liking a tweet and deleting a tweet as well. this is when i will have to pass in my token with every request to enable server trust my identity and simply identify me as the real user...

probably we wont use Cookie token the default django style, but a JWt(json web token).. so if so then thats it.

check AuthFrontend App for more details
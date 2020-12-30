# tweeter-DrfTest-httonlycookie
A tweeter clone build off of django, django rest framework with a httponly cookie application

# Stacks

1) Django 
2) Django Rest Framework
3) Vanilla js
4) XML for Ajax

# Story

story behind was to learn the DRF processes and how to build scalable apps(web and mobile) with it.
And i followed a course on building a "tweeter(twitter) clone app" from one of my best youtube tutour on django, Justin from codingforentrepreneurs(CFE).
And also brad traversy media on XMlHttpRequest js default ajax object.

And while building it, i decided to add an extra feature concerning security on token authentication that is,using "httponly" cookie with django, tookn weeks but it was fun as i learnt a whole new lot on security not just on token auth with Drf bbut for the web per say!!

Thanks to Justin Mitch from CFE and to Brad as well!!...


## Little info on httponly cookie with django, Drf and token auth...

** Django takes in user data.
** Authenticates to see if its valid and correct.
** creates a token in exchange for those credentials.
** pass the token as an httponly cookie disabling the effect of js on it preventing xss attacks from client side
** allow the server handle the authorization process since js can't.
** create a middleware to handle this as a middle man setting the headers before being passed on to the server completely.

follow me on twitter at https://twitter.com/Coding_mine
follow me on linkedin at https://www.linkedin.com/in/osagiede-harrison-2593b2202/
## More on the codes!!!...

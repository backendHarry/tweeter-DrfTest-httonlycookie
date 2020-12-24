so from the accounts readme file..

my first was to use localStorage first before implementing other methods..

simply get the token from a server response and set the item to localStorage..

localStorage.setItem('token', serverresponse.token) and that's it.

And since i'm using AJAX with xhr... 

you will have to set headers ..

simply as xhr.setHeader(.....) with an 'Authorization' and the 'Token "localStorage token"' and that's it..

check my thread at my twitter handle https://twitter.com/coding_mine where i discussed on my findings on these stuff, if found not correct please re-tweet with your own opinion as well.
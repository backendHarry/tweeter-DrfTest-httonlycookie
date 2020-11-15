# About Process...

following a course online on django and react for building a twitter clone, thanks to justin from 'codingforentreprenuers' on tweet-me project and he mentioned on us teaching others as well to see how well we understand the whole thing ..

## first part

starting off with the project involves the use of django and react ... django a full stack like framework thanks to jinja templating system that helps build backend strutures for a web project..

Due to the fact that its made up with python or as a differnt stack from frontend frameworks , its needs a process or a medium to help coonects these two and thats becomes the "API"

'API' Application programming interface helps makes the connection. well for django we should normally use the 'DRF' as it makes the whole process clean and easy ... but i will love to start from scratch and understand the whole process...

## Methods

there are lots of ways to go about it offcourse its js, but will try to follow up with ATLEAST 3..

## 1) XHR .. XMLHttpRequest..

creates a method which handles or acts likes the base block to all Apis.. 

it kind of creates a connection between the backend and the frontend with this methods ..

## open
## onload 
## send 

and they all try their best to get a result whhich is the response from the DB/server, offcourse relationship to frontend and backend its a 'REQUEST' and 'RESPONSE' relationships..

open starts the connection ...
onload becomes the process or result in between and after the connection..(it handles the logic , its acts like the bridge on both of them)
while send -> sends th request to the backend .


while making these requests, we will come across HttpRequests , 2 main types will be 'GET' and 'POST' request..


the GET is the simple request as it requires lesser security and just a fetch from the backend literally nothing else.. it makes no connection to the SERVER but to django which made sure to load the date already so, GET request wont make interactions to the DB..


but for POST the reverse of GET , it adds an additional method .. 
##SetRequestHeader which helps in making it work asynchronously ... and acts like how AJAX should and it also adds extra secure functions ....


## time to start building .....

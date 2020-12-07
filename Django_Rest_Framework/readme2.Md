# Using The Django Rest Framework.

before doing this , i followed Justin's tutorial on codingforentrepreneurs... and i've actually learnt alot.

## DRf

Drf -> Django Rest Framework works almost as pure vanilla Django for Apis , but reduces boilerplates and helps maintain the DRY principle for common patterns on the web with respect to how Apis are made.


# comparing with Vanilla Django and DRF Framework.

we all know base of what everyone needs in django or what revolves around django are
1) Models
2) Views
3) URLs.

The Drf framework makes sure it maintains the same concept nut not just that , it also adds something much better, SERIALIZERS..

so for the DRF, we now have

1) Models
2) SERIALIZERS
3) Views
4) Urls.

## Serializers.

what are serializers?, recall to bring the data from the DB, we did something like this
'''
QuerySet = Model.objects.all()
 data = [ {x.id, x.post, x...} for x in QuerySet ]
'''
and then passed data in JsonResponse.

well that was us converting what we had in the DB(model instance) and passing it to a Response that converts to JSON.

the main thing there is the idea of passing to Dictionary in python then passing to response.


well Serializer helps in doing that and much more .

1) first of it helps us do the transformation to dict data type automatically.
2) it helps us easily take data from the request and do the same thing.
3) it helps us validate data as well... 
HOW COOL!!!!.

## how does it look like.
Basic Serializer structure and Logic resembles that of forms you create from forms.py , and this alone makes it super cool , easy and fast to understand .. offcourse with little differences but not much for basic stuff ...which might act like whole stuff depending on how you write codes.

---->>>>[##Structure]
  class SomeSerializer(serializers.ModelSerializer):
        class Meta:
            model = SomeModel
            fields = [ ..... ]
            read_only_fields =[ .....]

looks similiar to 
    class SomeForm(forms.ModelForm):
            class Meta:
                model = SomeModel
                fields =[ ...]


that is because not only does it changes data to dict for Response to parse to json , it also works like the form .. infact just replace your forms with serializer when you see it, with some exceptions.


summary :: serializers = Data To Dict + Forms.


## In Views..
just as we have forms in views like i said serializers work like forms.

just as we have some logic for taking data in post form.

def some_view(request, *args, **kwargs):
    form = Form(request.POST)
    if form.is_valid():
        obj = form.save()
        return JsonResponse([ {obj.....}], status=201)

but with DRF

'# with some decorators '
def some_view(request, *...):
    serializer = SerializerClass(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

thats much of it.
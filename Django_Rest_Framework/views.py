from django.shortcuts import render
from .models import TweetPostDrf

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .serializers import TweetPostSerializer, TweetLikeSerializer
from .renderers import DataRenderer

#C
#R
#U
#D

#normally for clean code you will create Apis in a seperate folder and normal django rendering
#the template in another folder
def templateView(request):
    return render(request, 'Django_Rest_Framework/base.html')

#create view both cbv and fbv
class CreateView(generics.CreateAPIView):
    serializer_class = TweetPostSerializer

@api_view(['POST'])
# @renderer_classes([DataRenderer])  #renderers are used to affect the way you see data .
def createView(request, *args, **kwargs):
    serializer = TweetPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        if request.is_ajax():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#list view both cbv and fbv
class IndexView(generics.ListAPIView):
    serializer_class = TweetPostSerializer
    queryset = TweetPostDrf.objects.all()

    #methods you can override for classes. All classes not just this one
    #1) get_queryset()
    #2) get_object()
    #3) filter_queryset()
    #4) get_serialize_class()
    #5) perform_create()
    #6) perform_update()
    #7) perform_destroy()
    #8) get_serialzer_context()
    #9) get
    #10) post
    #11) list


@api_view(['GET'])
# @renderer_classes([DataRenderer])
def apiIndexView(request):
    qs = TweetPostDrf.objects.all()
    serializer = TweetPostSerializer(qs, many=True)
    return Response({'data_list':serializer.data}, status=200)


#update view for fbv and cbv
@api_view(['PUT'])
def updateView(request, id):
    #we fetch the db for the id/pk. and we can get use the "get_object_or_404" but we want react to handle everything
    try:
        qs = TweetPostDrf.objects.get(id=id)
    except TweetPostDrf.DoesNotExist:
        return Response({'message':'sorry, tweet does not exist'}, status=status.HTTP_404_NOT_FOUND)
    serializer = TweetPostSerializer(qs, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'message':'some other error occured'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(generics.UpdateAPIView):
    serializer_class = TweetPostSerializer
    lookup_field= 'pk'
    queryset = TweetPostDrf.objects.all()



@api_view(['DELETE'])
def deleteView(request, id):
    try:
        obj = TweetPostDrf.objects.get(id=id)
    except TweetPostDrf.DoesNotExist:
        return Response({'message':'sorry, tweet does not exist'}, status=status.HTTP_404_NOT_FOUND)
    obj.delete()
    return Response({'message':'tweet deleted'}, status=status.HTTP_204_NO_CONTENT)


class DeleteView(generics.DestroyAPIView):
    queryset = TweetPostDrf.objects.all()
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        return Response({'message':'Welcome, delete tweet'}, status=status.HTTP_200_OK)


#handle like method
'''
the like cant have a url lookup that gets the post id, so i will have to get yhe id from the post itself.
and its a post form, when the user clicks on the button it should send a post data which i will use in getting the id,  and will have to create a new serializer coz the old one helps creating a post which i'm not creating.
P.S i will be sending the Id through js.
'''

@api_view(['POST'])
def handleLike(request, *args, **kwargs):
    serializer = TweetLikeSerializer(data=request.data)
    if serializer.is_valid():
        data_id = serializer.validated_data.get('id') #instead of forms.cleaned_data
        obj = TweetPostDrf.objects.get(id=data_id)
        if not obj:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        if request.user in obj.likes.all():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)
    return Response({}, status=status.HTTP_200_OK)

# class handleLike(generics.ListCreateAPIView):
#     queryset = TweetPostDrf.objects.all()
#     serializer_class = TweetLikeSerializer
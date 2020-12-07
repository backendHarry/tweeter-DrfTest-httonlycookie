from rest_framework import serializers 
from .models import TweetPostDrf


class TweetLikeSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class TweetPostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TweetPostDrf
        fields =['id', 'post', 'likes']
        read_only_fields= ['id', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()
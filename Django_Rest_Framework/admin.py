from django.contrib import admin

# Register your models here.

from .models import TweetPostDrf, TweetLike

admin.site.register(TweetPostDrf)
admin.site.register(TweetLike)
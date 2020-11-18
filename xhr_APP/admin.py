from django.contrib import admin

# Register your models here.

from .models import TweetPost

admin.site.register(TweetPost)
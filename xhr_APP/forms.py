from django import forms

from .models import TweetPost

class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetPost
        fields = ['post', 'like']

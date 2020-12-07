from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class TweetPostDrf(models.Model):
    post = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, through='TweetLike', blank=True)

    def __str__(self):
        return self.post

    class Meta:
        ordering = ["-id"]

class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweetPost = models.ForeignKey(TweetPostDrf, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




# Note::
# for the like system we will have to use a many to m any field referencing users and posts
# User A can like Post 1
# User A can like post 2
# Post 1 can be liked by User A
# Post 1 can be liked by User B

# Many Post instances to Many User instances.. thanks to justin from CFE for the logic.

'''the post has a field called like which links to the model field, which is good as it is, but mot just we want the like to be independent if case you will want to attach time to it, that's why we use the through option, by default django handles the through logic and probably make it reference to a its own model , i.e the TweetPostDrf, but overrding that gives us access to create an intermediary between both models the 'User' and 'Post' meaning they are connected with the like field
'''

'''
    why do we always add a foreign key field when we do many to many relationship??,
    so it helps us manage logic of deleting one instance of a model to affec another .
'''

'''
more on the tweetlike model, an instance of the model/class now acts like a single like data containing other data, meaning if we want the total numbers of likes for an single post, you filter to that post and count likes from the post simply like Model.objects.filter(.....).count()
'''

'''so the trick is this , instead of adding a like field, we add an instance of a like model which appears as a field, so we will be adding an instance of the like to the user
first to access like we use TweetPostDrf which bears the like field
TweetPostDrf.objects.likes.first().add(user_instance)
'''
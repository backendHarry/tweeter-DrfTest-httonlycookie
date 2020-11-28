from django.db import models

# Create your models here.

class TweetPost(models.Model):
    post = models.CharField(max_length=200)
    like = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.post

    class Meta:
        ordering = ["-id"]

    # serializing the data to make it clean rather than the dictionary of {'post':...}

    def serializer(self):
        return {
            'id':self.id,
            'post':self.post,
            'like':self.like
        }

        
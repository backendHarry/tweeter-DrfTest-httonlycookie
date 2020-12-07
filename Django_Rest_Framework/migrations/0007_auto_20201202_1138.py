# Generated by Django 3.0.4 on 2020-12-02 19:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Django_Rest_Framework', '0006_remove_tweetlike_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetpostdrf',
            name='likes',
            field=models.ManyToManyField(blank=True, through='Django_Rest_Framework.TweetLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
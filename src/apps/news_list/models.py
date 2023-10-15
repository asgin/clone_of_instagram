from django.db import models
from apps.users.models import InstaUser

class Post(models.Model):
    photo = models.ImageField(upload_to='photo/')
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(InstaUser, on_delete=models.PROTECT)
    text = models.TextField(default='')

    @property
    def likes(self):
        return Likes.objects.filter(photo=self).count()

class Likes(models.Model):
    user = models.ForeignKey(InstaUser, on_delete=models.PROTECT)
    photo = models.ForeignKey(Post, on_delete=models.PROTECT)

class Subscribes(models.Model):
    follower = models.ForeignKey(InstaUser, on_delete=models.PROTECT, related_name='follower')
    following = models.ForeignKey(InstaUser, on_delete=models.PROTECT, related_name='following')
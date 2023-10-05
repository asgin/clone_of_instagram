from django.contrib import admin
from .models import Post, Likes, Subscribes

admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Subscribes)
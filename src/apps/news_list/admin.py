from django.contrib import admin
from apps.news_list.models import Post, Likes, Subscribes

admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Subscribes)
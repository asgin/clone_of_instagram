from django.http import HttpRequest
from apps.news_list.models import Post, Subscribes, Likes

def get_posts(request: HttpRequest) -> list:
    subs = Subscribes.objects.filter(follower_id=request.user.id)
    posts = []
    for i in subs.values_list('following_id'):
        posts += Post.objects.filter(user_id=i)
    return posts
        
def post_likes(request: HttpRequest, posts: list) -> list:
    list_of_likes = []
    for i in posts:
        if str(i.id) in request.POST:
            if not Likes.objects.filter(user_id=request.user.id, photo_id=i.id).exists():
                list_of_likes.append(Likes.objects.create(user_id=request.user.id, photo_id=i.id))
    return list_of_likes
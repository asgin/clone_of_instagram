from django.http import HttpRequest
from users.models import InstaUser
from news_list.models import Subscribes

def subscribe(request: HttpRequest, user: InstaUser) -> None:
    if 'subscribe' in request.POST:
        Subscribes.objects.create(follower_id=request.user.id, following_id=user.id)
    if 'unsubscribe' in request.POST:
        Subscribes.objects.filter(follower_id=request.user.id, following_id=user.id).delete()    

def subs_count(user: InstaUser) -> int:
    return Subscribes.objects.filter(following_id=user.id).count()
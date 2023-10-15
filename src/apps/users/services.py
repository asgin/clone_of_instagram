from django.http import HttpRequest
from apps.users.models import InstaUser
from apps.news_list.models import Subscribes

def subscribe(request: HttpRequest, user: InstaUser) -> Subscribes:
    if 'subscribe' in request.POST:
        sub = Subscribes.objects.create(follower_id=request.user.id, following_id=user.id)
        return sub
    if 'unsubscribe' in request.POST:
        sub = Subscribes.objects.filter(follower_id=request.user.id, following_id=user.id).first()
        sub.delete()
        return sub

def subs_count(user: InstaUser) -> int:
    return Subscribes.objects.filter(following_id=user.id).count()
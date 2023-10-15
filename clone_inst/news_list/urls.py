from django.urls import path
from .views import NewsList, AddPhoto
 
urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('add_photo/', AddPhoto.as_view(), name='add_photo'),
]
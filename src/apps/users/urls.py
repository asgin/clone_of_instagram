from apps.users.views import ProfileView, LoginView, ProfileView, home, RegisterView
from django.urls import include, path
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    path('registr/', RegisterView.as_view(), name='registr'),
    path('login/', LoginView.as_view(), name='login'),
    path('exit/', authViews.LogoutView.as_view(next_page='/login/'), name='exit'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('', home, name='home'),
    path('auth/', include('social_django.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from news_list.models import Post, Subscribes
from .forms import RegisterForm, LoginForm
from .models import InstaUser
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView
from .services import subs_count, subscribe


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/registr.html'

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        user = form.save(commit=False)
        user.link = f'http://127.0.0.1:8000/profile/{user.username}' 
        user.save()
        return redirect('http://127.0.0.1:8000/login/')

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(request, 'users/registr.html', {'form': form})
    
class LoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

class ProfileView(DetailView):
    template_name = 'users/profile.html'
    model = InstaUser
    context_object_name = 'user'

    def get_object(self):
        self.user = InstaUser.objects.get(username=self.kwargs['username'])
        return self.user
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user_id=self.user.id)
        context['subscribe'] = Subscribes.objects.filter(follower_id=self.request.user.id, following_id=self.user.id).exists()
        context['subs_count'] = subs_count(self.user)
        return context
    
    def post(self, request: HttpRequest, username: str) -> HttpResponse:
        user = InstaUser.objects.get(username=username)
        subscribe(request, user)
        return redirect(f'http://127.0.0.1:8000/profile/{username}')

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'users/home.html')
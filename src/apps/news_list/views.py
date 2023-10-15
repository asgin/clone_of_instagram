from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, CreateView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from apps.news_list.models import Post
from apps.news_list.forms import PostForm
from django.utils.decorators import method_decorator
from apps.news_list.services import get_posts, post_likes

@method_decorator(login_required, name='dispatch')
class NewsList(ListView):
    model = Post
    template_name = 'news_list/news.html'
    context_object_name = 'posts'

    def get_queryset(self) -> list:
        self.queryset = get_posts(self.request)
        return self.queryset
    
    def post(self, request: HttpRequest) -> HttpResponse:
        post_likes(request=request, posts=get_posts(request=request))
        return redirect('http://127.0.0.1:8000/news/')

@method_decorator(login_required, name='dispatch')   
class AddPhoto(CreateView):
    template_name = 'news_list/photo_add.html'
    form_class = PostForm

    def form_valid(self, form: PostForm) -> HttpResponse:
        forma = form.save(commit=False)
        forma.user = self.request.user
        forma.save()
        return HttpResponse('Пост успешно добавлен!')
from django import forms
from apps.news_list.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'text']
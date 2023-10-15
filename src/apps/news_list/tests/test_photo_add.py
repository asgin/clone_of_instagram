from django.test import TestCase
from apps.news_list.models import Post
from apps.users.models import InstaUser

class TestAddPhoto(TestCase):

    def setUp(self) -> None:
        self.user = InstaUser.objects.create_user(username='testuser', password='password')


    def test_add_photo(self):
        self.client.login(username='testuser', password='password')
        with open('media/photo/40CM0z-oWOg.jpg', 'rb') as photo:
            self.client.post('/add_photo/', {'photo': photo, 'text':'text'})
            self.assertTrue(Post.objects.filter(text='text').exists())
    
    def test_add_photo_fail(self):
        with open('media/photo/40CM0z-oWOg.jpg', 'rb') as photo:
            self.client.post('/add_photo/', {'photo': photo, 'text':'text'})
            self.assertFalse(Post.objects.filter(text='text').exists())
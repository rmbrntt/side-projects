from django.test import TestCase
from blog_app.models import Post
# Create your tests here.

class PostTests(TestCase):

    def test_str(self):

        my_title = Post(title='This is a title to test')
        self.assertEqual(str(my_title), 'This is a title to test')


from django.test import SimpleTestCase
from blogapp.service import get_all_blog_titles
from djangomockingbird.decorator import mock_model

from blogapp.models import BlogPost
import blogapp


# Create your tests here.

class ServiceTestCase(SimpleTestCase):
    

    @mock_model('blogapp.service.BlogPost', specs={'title':'hello'})
    def test_get_all_blog_titles(self):
        blog_titles = get_all_blog_titles()
        self.assertEqual(blog_titles, ['hello'])
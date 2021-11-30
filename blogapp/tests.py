from django.test import SimpleTestCase
from blogapp.service import get_all_blog_titles
from djangomockingbird.make_mocks import make_mocks
from blogapp.models import BlogPost
import blogapp


# Create your tests here.

class ServiceTestCase(SimpleTestCase):

    def test_get_all_blog_titles(self):
        blogapp.service.BlogPost = make_mocks(BlogPost, specs={'title':'hello'})
        blog_titles = get_all_blog_titles()
        self.assertEqual(blog_titles, ['hello'])
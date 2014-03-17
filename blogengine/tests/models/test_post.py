from django.test import TestCase

from blogengine.models import Post
from blogengine.tests.unittest_support import create_post, create_user, create_site

class PostTest(TestCase):
    def test_create_post(self):
        # Creates the author
        author = create_user()

        # Create a site
        site = create_site()

        # Creates the Post with some attributes
        post = create_post(author, site)

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Checks attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)
        self.assertEquals(only_post.author, author)

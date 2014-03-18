from django.test import TestCase

from blogengine.models import Post, Category
from blogengine.tests.unittest_support import *

class PostTest(TestCase):
    def setUp(self):
        self.post = create_test_post()
        self.tag = create_tag()
        self.post.tags.add(self.tag)
        self.post.save()

    def test_create_post(self):
        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, self.post)

        # Checks attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.pub_date.day, self.post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, self.post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, self.post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, self.post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, self.post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, self.post.pub_date.second)
        self.assertEquals(only_post.author, self.post.author)
        self.assertEquals(only_post.category, self.post.category)

        # Check tags
        post_tags = only_post.tags.all()
        self.assertEquals(len(post_tags), 1)
        only_post_tag = post_tags[0]
        self.assertEquals(only_post_tag, self.tag)
        self.assertEquals(only_post_tag.name, 'python')
        self.assertEquals(only_post_tag.description, 'The Python programming lanaguage')

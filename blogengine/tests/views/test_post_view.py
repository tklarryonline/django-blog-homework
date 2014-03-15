import markdown
from django.test import LiveServerTestCase, Client

from blogengine.models import Post
from blogengine.tests.unittest_support import create_post

class PostViewTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        post = create_post(title='My first post',
                           text='This is [my first blog post](http://localhost:8000/)')

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

        # Fetches the index page
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        # Checks if the post data is in the response
        self.assertTrue(post.title in response.content)
        self.assertTrue(markdown.markdown(post.text) in response.content)
        self.assertTrue(str(post.pub_date.year) in response.content)
        self.assertTrue(post.pub_date.strftime('%b') in response.content)
        self.assertTrue(str(post.pub_date.day) in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

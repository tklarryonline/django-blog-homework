import markdown

from blogengine.models import Post
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import create_post, create_user

class PostViewTest(BaseAcceptanceTest):
    def test_index(self):
        # Creates the author
        author = create_user()

        # Creates post
        post = create_post(author=author,
                           title='My first post',
                           text='This is [my first blog post](http://localhost:8000/)')

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

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

    def test_post_page(self):
        # Creates the author
        author = create_user()

        # Creates post
        post = create_post(author=author,
                           title='My first post',
                           text='This is [my first blog post](http://localhost:8000/)')

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Gets the post URL
        post_url = only_post.get_absolute_url()

        # Fetches the post
        response = self.client.get(post_url)
        self.assertEquals(response.status_code, 200)

        # Checks if the post data is in the response
        self.assertTrue(post.title in response.content)
        self.assertTrue(markdown.markdown(post.text) in response.content)
        self.assertTrue(str(post.pub_date.year) in response.content)
        self.assertTrue(post.pub_date.strftime('%b') in response.content)
        self.assertTrue(str(post.pub_date.day) in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

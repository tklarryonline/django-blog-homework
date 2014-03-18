import markdown

from blogengine.models import Post
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import *

class PostViewTest(BaseAcceptanceTest):
    def test_index(self):
        # Creates the author
        author = create_user()

        # Create a site
        site = create_site()

        # Create a category
        category = create_category()

        # Creates post
        post = create_post(author=author, site=site, category=category,
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
        self.assertTrue(post.category.name in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

    def test_post_page(self):
        # Creates the author
        author = create_user()

        # Create a site
        site = create_site()

        # Create a category
        category = create_category()

        # Creates post
        post = create_post(author=author, site=site, category=category,
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
        self.assertTrue(post.category.name in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

    def test_category_page(self):
        # Creates the author
        author = create_user()

        # Create a site
        site = create_site()

        # Create a category
        category = create_category()

        # Creates post
        post = create_post(author=author, site=site, category=category,
                           title='My first post',
                           text='This is [my first blog post](http://localhost:8000/)')

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Gets the category URL
        category_url = post.category.get_absolute_url()

        # Fetches the category
        response = self.client.get(category_url)
        self.assertEquals(response.status_code, 200)

        # Checks if the category data is in the response
        self.assertTrue(post.category.name in response.content)

        # Checks if the post is appear in the response
        self.assertTrue(post.title in response.content)
        self.assertTrue(markdown.markdown(post.text) in response.content)
        self.assertTrue(str(post.pub_date.year) in response.content)
        self.assertTrue(post.pub_date.strftime('%b') in response.content)
        self.assertTrue(str(post.pub_date.day) in response.content)
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

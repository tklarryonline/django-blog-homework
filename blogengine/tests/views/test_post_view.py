import markdown

from blogengine.models import Post
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import *


class PostViewTest(BaseAcceptanceTest):
    def set_up_post(self):
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

        # Tag the post
        tag = create_tag()
        post.tags.add(tag)
        post.save()

        return post

    def test_index(self):
        # Creates post
        post = self.set_up_post()

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

        # Checks if the post category is in the response
        self.assertTrue(post.category.name in response.content)

        # Checks if the post tag is in the response
        post_tag = only_post.tags.all()[0]
        self.assertTrue(post_tag.name in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

    def test_post_page(self):
        # Creates post
        post = self.set_up_post()

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

        # Checks if the post category is in the response
        self.assertTrue(post.category.name in response.content)

        # Checks if the post tag is in the response
        post_tag = only_post.tags.all()[0]
        self.assertTrue(post_tag.name in response.content)

        # Checks if the link is marked up properly
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

    def test_category_page(self):
        # Creates post
        post = self.set_up_post()

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

    def test_tag_page(self):
        # Creates post
        post = self.set_up_post()

        # Checks if post is created successfully
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Gets the post's first tag
        post_tag = only_post.tags.all()[0]

        # Gets the tag URL
        tag_url = post_tag.get_absolute_url()

        # Fetches the tag
        response = self.client.get(tag_url)
        self.assertEquals(response.status_code, 200)

        # Checks if the tag data is in the response
        self.assertTrue(post_tag.name in response.content)

        # Checks if the post is appear in the response
        self.assertTrue(post.title in response.content)
        self.assertTrue(markdown.markdown(post.text) in response.content)
        self.assertTrue(str(post.pub_date.year) in response.content)
        self.assertTrue(post.pub_date.strftime('%b') in response.content)
        self.assertTrue(str(post.pub_date.day) in response.content)
        self.assertTrue('<a href="http://localhost:8000/">my first blog post</a>' in response.content)

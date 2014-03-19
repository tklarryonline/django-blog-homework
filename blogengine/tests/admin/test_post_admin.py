from django.utils.text import slugify

from blogengine.models import Post
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import create_category, create_tag
from blogengine.tests.unittest_support import create_test_post


class PostAdminTest(BaseAcceptanceTest):
    def set_up_post(self):
        # Set up post
        self.post = create_test_post()
        self.tag = create_tag()
        self.post.tags.add(self.tag)
        self.post.save()

    def test_create_post(self):
        # Create the category
        create_category()

        # Create the tag
        create_tag()

        # Logs in first
        self.client.login(username="luannguyen", password="password")

        # Checks the response
        response = self.client.get('/admin/blogengine/post/add/')
        self.assertEquals(response.status_code, 200)

        # Creates a new post
        response = self.client.post('/admin/blogengine/post/add/', {
            'title': 'My first post',
            'text': 'This is my first post',
            'pub_date_0': '2014-03-15',
            'pub_date_1': '1:00:32',
            'slug': slugify(u'My first post'),
            'site': '1',
            'category': '1',
            'tags': '1'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Checks message from response
        self.assertTrue('added successfully' in response.content)

        # Checks new post in database
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

    def test_edit_post(self):
        # Setup post
        self.set_up_post()

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Edit the post
        response = self.client.post('/admin/blogengine/post/1/', {
            'title': 'My second post',
            'text': 'This is my second blog post',
            'pub_date_0': '2013-12-28',
            'pub_date_1': '22:00:04',
            'slug': slugify(u'My first post'),
            'site': '1',
            'category': '1',
            'tags': '1'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check changed successfully
        self.assertTrue('changed successfully' in response.content)

        # Check post amended
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        post = all_posts[0]
        self.assertEquals(post.title, 'My second post')
        self.assertEquals(post.text, 'This is my second blog post')

    def test_delete_post(self):
        # Setup post
        self.set_up_post()

        # Check new post saved
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Delete the post
        response = self.client.post('/admin/blogengine/post/1/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue('deleted successfully' in response.content)

        # Check post deleted from database
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 0)

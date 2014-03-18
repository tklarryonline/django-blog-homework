from django.utils.text import slugify

from blogengine.models import Post, Category
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import *


class AdminTest(BaseAcceptanceTest):
    def test_login(self):
        # Gets login page
        response = self.client.get('/admin/')

        # Checks response
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log in' in response.content)

        # Logs the user in
        login = self.client.login(username="luannguyen", password="password")

        # Checks if the login is successful
        self.assertTrue(login)

        # Checks the response again
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        # Logs in first
        self.client.login(username="luannguyen", password="password")

        # Checks the response
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)

        # Now logs out
        self.client.logout()

        # Checks the response again
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log in' in response.content)


class PostAdminTest(BaseAcceptanceTest):
    def set_up_post(self):
        # Set up post
        self.post = create_test_post()
        self.tag = create_tag()
        self.post.tags.add(self.tag)
        self.post.save()

    def test_create_post(self):
        # Create the category
        category = create_category()

        # Create the tag
        tag = create_tag()

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


class CategoryAdminTest(BaseAcceptanceTest):
    def test_create_category(self):
        # Logs in first
        self.client.login(username="luannguyen", password="password")

        # Checks the response
        response = self.client.get('/admin/blogengine/category/add/')
        self.assertEquals(response.status_code, 200)

        # Creates a new category
        response = self.client.post('/admin/blogengine/category/add/', {
            'name': 'python',
            'description': 'The Python programming lanaguage'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Checks message from response
        self.assertTrue('added successfully' in response.content)

        # Checks new category in database
        all_categories = Category.objects.all()
        self.assertEquals(len(all_categories), 1)

    def test_edit_category(self):
        # Create a category
        category = create_category()

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Edit the category
        response = self.client.post('/admin/blogengine/category/1/', {
            'name': 'perl',
            'description': 'The Perl programming lanaguage'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check changed successfully
        self.assertTrue('changed successfully' in response.content)

        # Checks new category in database
        all_categories = Category.objects.all()
        self.assertEquals(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEquals(only_category.name, 'perl')
        self.assertEquals(only_category.description, 'The Perl programming lanaguage')

    def test_delete_category(self):
        # Create a category
        category = create_category()

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Delete the category
        response = self.client.post('/admin/blogengine/category/1/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue('deleted successfully' in response.content)

        # Check category amended
        all_categories = Category.objects.all()
        self.assertEquals(len(all_categories), 0)

class TagAdminTest(BaseAcceptanceTest):
    def test_create_tag(self):
        # Logs in first
        self.client.login(username="luannguyen", password="password")

        # Checks the response
        response = self.client.get('/admin/blogengine/tag/add/')
        self.assertEquals(response.status_code, 200)

        # Creates a new tag
        response = self.client.post('/admin/blogengine/tag/add/', {
            'name': 'python',
            'description': 'The Python programming lanaguage'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Checks message from response
        self.assertTrue('added successfully' in response.content)

        # Checks new tag in database
        all_tags = Tag.objects.all()
        self.assertEquals(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEquals(only_tag.name, 'python')
        self.assertEquals(only_tag.description, 'The Python programming lanaguage')

    def test_edit_tag(self):
        # Create a tag
        tag = create_tag()

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Edit the tag
        response = self.client.post('/admin/blogengine/tag/1/', {
            'name': 'perl',
            'description': 'The Perl programming lanaguage'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check changed successfully
        self.assertTrue('changed successfully' in response.content)

        # Checks new tag in database
        all_tags = Tag.objects.all()
        self.assertEquals(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEquals(only_tag.name, 'perl')
        self.assertEquals(only_tag.description, 'The Perl programming lanaguage')

    def test_delete_tag(self):
        # Create a tag
        tag = create_tag()

        # Log in
        self.client.login(username='luannguyen', password="password")

        # Delete the tag
        response = self.client.post('/admin/blogengine/tag/1/delete/', {
            'post': 'yes'
        }, follow=True)
        self.assertEquals(response.status_code, 200)

        # Check deleted successfully
        self.assertTrue('deleted successfully' in response.content)

        # Checks tag is deleted in database
        all_tags = Tag.objects.all()
        self.assertEquals(len(all_tags), 0)

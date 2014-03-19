from blogengine.models import Tag
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import create_tag


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
        self.assertEquals(only_tag.description,
                          'The Python programming lanaguage')

    def test_edit_tag(self):
        # Create a tag
        create_tag()

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
        self.assertEquals(only_tag.description,
                          'The Perl programming lanaguage')

    def test_delete_tag(self):
        # Create a tag
        create_tag()

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

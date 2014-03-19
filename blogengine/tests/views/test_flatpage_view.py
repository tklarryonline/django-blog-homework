from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest


class FlatPageViewTest(BaseAcceptanceTest):
    def create_flat_page(self, url, title, content):
        page = FlatPage.objects.create(url=url, title=title, content=content)
        page.sites.add(Site.objects.all()[0])
        page.save()
        return page

    def test_create_flat_page(self):
        page = self.create_flat_page(url='/about/',
                                     title='About me',
                                     content='All about me')

        # Checks if the new page saved
        all_pages = FlatPage.objects.all()
        self.assertEquals(len(all_pages), 1)
        only_page = all_pages[0]
        self.assertEquals(only_page, page)

        # Checks if the data is correct
        self.assertEquals(only_page.url, '/about/')
        self.assertEquals(only_page.title, 'About me')
        self.assertEquals(only_page.content, 'All about me')

        # Gets the URL
        page_url = only_page.get_absolute_url()
        response = self.client.get(page_url)

        # Checks the response
        response = self.client.get(page_url)
        self.assertEquals(response.status_code, 200)

        # Check title and content in response
        self.assertTrue('About me' in response.content)
        self.assertTrue('All about me' in response.content)

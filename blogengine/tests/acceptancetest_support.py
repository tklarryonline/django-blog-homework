from django.test import LiveServerTestCase, Client

class BaseAcceptanceTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

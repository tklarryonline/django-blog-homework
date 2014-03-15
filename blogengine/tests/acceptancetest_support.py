from django.test import LiveServerTestCase, Client

class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()

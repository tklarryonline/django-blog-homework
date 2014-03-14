from django.test import LiveServerTestCase, Client

class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.client = Client()

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

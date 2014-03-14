from django.test import LiveServerTestCase, Client

class AdminTest(LiveServerTestCase):
    fixtures = ['users.json']

    def test_login(self):
        client = Client()

        # Gets login page
        response = client.get('/admin/')

        # Checks response
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log in' in response.content)

        # Logs the user in
        login = client.login(username="luannguyen", password="password")

        # Checks if the login is successful
        self.assertTrue(login)

        # Checks the response again
        response = client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)

    def test_logout(self):
        client = Client()

        # Logs in first
        client.login(username="luannguyen", password="password")

        # Checks the response
        response = client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log out' in response.content)

        # Now logs out
        client.logout()

        # Checks the response again
        response = client.get('/admin/')
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Log in' in response.content)

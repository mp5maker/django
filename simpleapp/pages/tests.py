from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/home')
        self.assertTrue(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/about')
        self.assertTrue(response.status_code, 200)

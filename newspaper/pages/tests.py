from django.test import TestCase

from django.urls import reverse

class HomePageViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get('')
        self.reverseResponse = self.client.get(reverse('pages:home'))

    def test_home_page_view(self):
        self.assertTrue(self.response.status_code, 200)
        self.assertTrue(self.reverseResponse.status_code, 200)
        self.assertTemplateUsed(self.response, 'pages/home.html')
        self.assertTemplateUsed(self.reverseResponse, 'pages/home.html')
from django.test import TestCase

from django.urls import reverse

class SignUpViewTest(TestCase):
    def setUp(self):
        self.url = self.client.get('accounts/signup')
        self.reverseUrl = self.client.get(reverse('accounts:signup'))
    
    def test_sign_up_view_test(self):
        self.assertTrue(self.url.status_code, 200)
        self.assertTrue(self.reverseUrl.status_code, 200)
        self.assertTemplateUsed('accounts/signup.html')
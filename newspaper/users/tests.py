from django.test import TestCase

from django.urls import reverse

from .models import CustomUser


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="test",
            email="khan.photon@gmail.com",
            password="test1234"
        )

        self.createdUser = list(CustomUser.objects.values().filter(id=1))

    def test_custom_user_model(self):
        self.assertTrue(len(self.createdUser), 1)
        self.assertTrue(self.createdUser[0]['username'],  'test')
        self.assertTrue(self.createdUser[0]['email'],  'khan.photon@gmail.com')
        self.assertTrue(self.createdUser[0]['password'],  'test1234')

class LoginPageViewTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/uusers/login/')
        self.reverseResponse = self.client.get(reverse('login'))

    def test_login_page_view(self):
        self.assertTrue(self.response.status_code, 200)
        self.assertTrue(self.reverseResponse.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/login.html')
        self.assertTemplateUsed(self.reverseResponse, 'registration/login.html')
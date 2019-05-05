from django.test import TestCase

from django.utils.timezone import now

from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

from django.urls import reverse

from .models import Post

from .views import PostHomeViewPage


class PostModelTest(TestCase):
    def setUp(self):
        self.text = 'just a text'
        self.slug = slugify(self.text)
        self.created_at = now()
        self.updated_at = now()

        Post.objects.create(
            text=self.text,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_text_content(self):
        post = Post.objects.values().filter(id=1)
        post = list(post)[0]
        self.assertTrue(post['text'], self.text)
        self.assertTrue(post['slug'], self.slug)
        self.assertTrue(post['created_at'], self.created_at)
        self.assertTrue(post['updated_at'], self.updated_at)


class PostHomeViewPageTest(TestCase):
    def setUp(self):
        self.text = 'just a text'
        self.slug = slugify(self.text)
        self.created_at = now()
        self.updated_at = now()

        Post.objects.create(
            text=self.text,
            slug=self.slug,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

        self.create_user = User.objects.create_user(
            username="test",
            email="test@gmail.com",
            password="secret78"
        )

        self.login_user = self.client.post(reverse('login'), {
            "username": "test",
            "password": "secret78"
        })

    def text_view_url_exists_at_proper_location(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        url = reverse('posts:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/home.html')

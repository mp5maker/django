from django.test import TestCase

from django.template.defaultfilters import slugify

from django.utils.timezone import now

from django.contrib.auth import get_user_model

from django.urls import reverse

from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.title = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. \
            Aliquid voluptatibus dolor libero sint omnis \
            obcaecati quibusdam quidem dolore temporibus ea."
        self.slug = slugify(self.title[:25])
        self.author = get_user_model().objects.create(
            username="test",
            email="test@gmail.com",
            password="secret79"
        )
        self.body = "testing the body"
        self.created_at = now()
        self.updated_at = now()
        self.post = Post.objects.create(
            title=self.title,
            slug=self.slug,
            author=self.author,
            body=self.body,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def test_object_created_with_post(self):
        post = list(Post.objects.values().filter(slug=self.slug))[0]
        author_id = list(get_user_model().objects.filter(username=self.author))[0].id
        self.assertEqual(post['title'], self.title)
        self.assertEqual(post['slug'], self.slug)
        self.assertEqual(post['author_id'], author_id)
        self.assertEqual(post['body'], self.body)
        self.assertEqual(post['created_at'], self.created_at)
        self.assertEqual(post['updated_at'], self.updated_at)

    def test_get_absolute_url(self):
        self.assertTrue(self.post.get_absolute_url(),
            'blogs/' + self.slug + "/"
        )


class BlogListPageViewTest(TestCase):
    def setUp(self):
        self.title = "this is just a test"
        self.slug = slugify(self.title[:25])
        self.author = get_user_model().objects.create(
            username="test",
            email="test@gmail.com",
            password="secret79"
        )
        self.body = "testing the body"
        self.created_at = now()
        self.updated_at = now()
        self.post = Post.objects.create(
            title=self.title,
            slug=self.slug,
            author=self.author,
            body=self.body,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
        self.url = self.client.get('/blogs/')
        self.reverseUrl = self.client.get(reverse('blogs:list'))

    def test_blog_list_page_view(self):
        self.assertTrue(self.url.status_code, 200)
        self.assertTrue(self.reverseUrl.status_code, 200)
        self.assertTemplateUsed(self.url, 'blogs/home.html')
        self.assertTemplateUsed(self.reverseUrl, 'blogs/home.html')
        self.assertContains(self.url, 'testing the body')
        self.assertContains(self.reverseUrl, 'testing the body')


class BlogDetailPageViewTest(TestCase):
    def setUp(self):
        self.title = "this is just a test"
        self.slug = slugify(self.title[:25])
        self.author = get_user_model().objects.create(
            username='test',
            email='test@gmail.com',
            password="secret78"
        )
        self.body="testing the body"
        self.created_at = now()
        self.updated_at = now()
        self.post = Post.objects.create(
            title=self.title,
            slug=self.slug,
            author=self.author,
            body=self.body,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
        self.url=self.client.get('/blogs/' + self.slug + "/")
        self.reverseUrl = self.client.get(
            reverse("blogs:details", kwargs={"slug": self.slug})
        )

    def test_blog_detail_page_view(self):
        no_response = self.client.get('/blogs/100')
        no_response_reverse = self.client.get(reverse('blogs:details', kwargs={"slug": "boom"}))
        self.assertTrue(self.url.status_code, 200)
        self.assertTrue(self.reverseUrl.status_code, 200)
        self.assertTemplateUsed(self.url, 'blogs/details.html')
        self.assertTemplateUsed(self.reverseUrl, 'blogs/details.html')
        self.assertContains(self.reverseUrl, 'testing the body')
        self.assertTrue(no_response, 404)
        self.assertTrue(no_response_reverse, 404)

class BlogCreatePageViewTest(TestCase):
    def setUp(self):
        self.title ="this is just a test"
        self.author = get_user_model().objects.create(
            username="test",
            email="test@gmail.com",
            password="secret89"
        )
        self.body="great day"
        self.response = self.client.post(reverse('blogs:create'), {
            "title": self.title,
            "body": self.body,
            "author": self.author
        })

    def test_blog_create_page_view(self):
        create_page_view = self.client.get(reverse('blogs:create'))
        self.assertTrue(create_page_view.status_code, 200)
        self.assertTemplateUsed(create_page_view, 'blogs/create.html')
        self.assertTrue(self.client.get(reverse('blogs:create')).status_code, 200)
        self.assertTrue(self.response.status_code, 200)
        self.assertContains(self.response, self.title)
        self.assertContains(self.response, self.body)

class BlogUpdatePageViewTest(TestCase):
    def setUp(self):
        self.title = "this is just a test"
        self.body = "boom shakalaka"
        self.slug = slugify(self.title[:25])
        self.author = get_user_model().objects.create(
            username="test",
            email="khan@gmail.com",
            password="secret78"
        )
        self.post = Post.objects.create(
            title=self.title,
            body=self.body,
            author=self.author
        )
        self.response = self.client.post(reverse('blogs:update',
            kwargs={"slug" : self.slug}), {
            "title": "this is updated test",
            "body": "Boom has been eliminated"
        })

    def test_blog_update_page_view(self):
        self.assertTrue(self.response.status_code, 302)
        self.assertContains(self.response, 'this is updated test')
        self.assertContains(self.response, 'Boom has been eliminated')

class BlogDeletePageViewTest(TestCase):
    def setUp(self):
        self.title = "this is just a test"
        self.body = "boom shakalaka"
        self.slug = slugify(self.title[:25])
        self.author = get_user_model().objects.create(
            username="test",
            email="khan@gmail.com",
            password="secret78"
        )
        self.post = Post.objects.create(
            title=self.title,
            body=self.body,
            author=self.author
        )
    def test_blog_delete_page_view(self):
        delete_page = self.client.get(reverse('blogs:delete', kwargs={"slug": self.slug}))
        response = self.client.post(reverse('blogs:delete', kwargs={"slug": self.slug}))
        self.assertTrue(delete_page.status_code, 200)
        self.assertTemplateUsed(delete_page, 'blogs/delete.html')
        self.assertTrue(response.status_code, 302)

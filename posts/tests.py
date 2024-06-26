from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Assuming you also need to provide an author for the foreign key relationship.
        user = User.objects.create_user(username='testuser', password='12345')
        cls.post = Post.objects.create(title="Sample Title", author=user, body="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.body, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/news/")
        self.assertEqual(response.status_code, 200)

    def test_news_page(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news.html")
        self.assertContains(response, "This is a test!")

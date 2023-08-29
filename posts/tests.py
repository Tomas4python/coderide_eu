from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.post = Post.objects.create(text="This is a test!")

	def test_model_content(self):
		self.assertEqual(self.post.text, "This is a test!")

	def test_url_exists_at_correct_location(self):
		response = self.client.get("/news/")
		self.assertEqual(response.status_code, 200)

	def test_news_page(self):
		response = self.client.get(reverse("news"))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, "news.html")
		self.assertContains(response, "This is a test!")

from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("home"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("home"))
		self.assertTemplateUsed(response, "home.html")

	def test_template_content(self):
		response = self.client.get(reverse("home"))
		self.assertContains(response, "<h1>My Code Ride</h1>")

class ThispageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/this/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("this"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("this"))
		self.assertTemplateUsed(response, "this_site.html")

	def test_template_content(self):
		response = self.client.get(reverse("this"))
		self.assertContains(response, "<h1>This Site</h1>")

class GamepageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/game/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("game"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("game"))
		self.assertTemplateUsed(response, "game.html")

	def test_template_content(self):
		response = self.client.get(reverse("game"))
		self.assertContains(response, "<h1>The Game</h1>")

class MeteopageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/meteo/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("meteo"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("meteo"))
		self.assertTemplateUsed(response, "meteo.html")

	def test_template_content(self):
		response = self.client.get(reverse("meteo"))
		self.assertContains(response, "<h1>Meteo App</h1>")

class ScrapingpageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/scraping/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("scraping"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("scraping"))
		self.assertTemplateUsed(response, "scraping.html")

	def test_template_content(self):
		response = self.client.get(reverse("scraping"))
		self.assertContains(response, "<h1>Web Scraping App</h1>")

class RispageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/ris/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("ris"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("ris"))
		self.assertTemplateUsed(response, "ris.html")

	def test_template_content(self):
		response = self.client.get(reverse("ris"))
		self.assertContains(response, "<h1>Reverse Image Search</h1>")

class ChatbotpageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/chatbot/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("chatbot"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("chatbot"))
		self.assertTemplateUsed(response, "chatbot.html")

	def test_template_content(self):
		response = self.client.get(reverse("chatbot"))
		self.assertContains(response, "<h1>ChatBot</h1>")

class SqlitepageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/sqlite/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("sqlite"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("sqlitet"))
		self.assertTemplateUsed(response, "sqlite.html")

	def test_template_content(self):
		response = self.client.get(reverse("sqlite"))
		self.assertContains(response, "<h1>SQLite</h1>")

class ImgslcpageTests(SimpleTestCase):
	def test_url_exists_at_correct_location(self):
		response = self.client.get("/imgslc/")
		self.assertEqual(response.status_code, 200)

	def test_url_available_by_name(self):
		response = self.client.get(reverse("imgslc"))
		self.assertEqual(response.status_code, 200)

	def test_template_name_correct(self):
		response = self.client.get(reverse("imgslc"))
		self.assertTemplateUsed(response, "imgslc.html")

	def test_template_content(self):
		response = self.client.get(reverse("imgslc"))
		self.assertContains(response, "<h1>Imgslc</h1>")
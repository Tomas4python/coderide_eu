from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = "home.html"

class ThisPageView(TemplateView):
	template_name = "this_site.html"

class GamePageView(TemplateView):
	template_name = "game.html"

class MeteoPageView(TemplateView):
	template_name = "meteo.html"

class ScrapingPageView(TemplateView):
	template_name = "scraping.html"

class RisPageView(TemplateView):
	template_name = "ris.html"

class ChatbotPageView(TemplateView):
	template_name = "chatbot.html"

class SqlitePageView(TemplateView):
	template_name = "sqlite.html"

class ImgslcPageView(TemplateView):
	template_name = "imgslc.html"

class SkillsPageView(TemplateView):
	template_name = "skills.html"
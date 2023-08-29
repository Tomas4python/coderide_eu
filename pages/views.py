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
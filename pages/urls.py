from django.urls import path
from .views import HomePageView, ThisPageView, GamePageView, MeteoPageView, ScrapingPageView
from django.conf.urls.static import static


urlpatterns = [
		path("", HomePageView.as_view(), name="home"),
		path("this/", ThisPageView.as_view(), name="this"),
		path("game/", GamePageView.as_view(), name="game"),
		path("meteo/", MeteoPageView.as_view(), name="meteo"),
		path("scraping/", ScrapingPageView.as_view(), name="scraping"),
		]
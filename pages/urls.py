from django.urls import path
from .views import HomePageView, ThisPageView, GamePageView, MeteoPageView, ScrapingPageView, RisPageView, ChatbotPageView, SqlitePageView, ImgslcPageView, SkillsPageView
from django.conf.urls.static import static


urlpatterns = [
		path("", HomePageView.as_view(), name="home"),
		path("skills/", SkillsPageView.as_view(), name="skills"),
		path("this/", ThisPageView.as_view(), name="this"),
		path("game/", GamePageView.as_view(), name="game"),
		path("meteo/", MeteoPageView.as_view(), name="meteo"),
		path("imgslc/", ImgslcPageView.as_view(), name="imgslc"),
		path("scraping/", ScrapingPageView.as_view(), name="scraping"),
		path("sqlite/", SqlitePageView.as_view(), name="sqlite"),
		path("ris/", RisPageView.as_view(), name="ris"),
		path("chatbot/", ChatbotPageView.as_view(), name="chatbot"),
		]
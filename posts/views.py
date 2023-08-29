from django.views.generic import ListView
from .models import Post

class NewsPageView(ListView):
	model = Post
	template_name = "news.html"
	queryset = Post.objects.all().order_by('-created_at')

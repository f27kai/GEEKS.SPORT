from django.views.generic import TemplateView, ListView
from catalog.models import Product
from .models import Slogan, YouTube


class HomeView(TemplateView):
    template_name = "sport/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slogan'] = Slogan.objects.first()
        context['popular_products'] = Product.objects.order_by('-rating')[:5]
        youtube_videos = YouTube.objects.all()
        youtube_data = []
        for video in youtube_videos:
            video_id = video.url_youtube.split('v=')[-1]
            youtube_data.append({
                'url': f'https://www.youtube.com/embed/{video_id}',
                'slogan': video.slogan.text
            })

        context['youtube_videos'] = youtube_data
        return context

class AboutUsView(TemplateView):
    template_name = 'sport/about_us.html'

class ContactView(TemplateView):
    template_name = 'sport/contact.html'

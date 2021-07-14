"""allinone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path('secret-vin/', admin.site.urls),
    path('', views.index),
    path('age-calculator/', include('agecalci.urls')),
    path('contact/', include('contact.urls')),
    path('blogs/', include('blog.urls')),
    path('calculator/', include('calculator.urls')),
    path('currencyconverter/', include('currencyconverter.urls')),
    path('instaimagedownloader/', include('instaimagedown.urls')),
    path('number-guess-game/', include('numguess.urls')),
    path('password-generator/', include('passwordgenr.urls')),
    path('pdf-to-word-converter/', include('pdftoword.urls')),
    path('rock-paper-scizer-game/', include('rockpaperscizer.urls')),
    path('social/', include('social.urls')),
    path('text-utility/', include('textutils.urls')),
    path('tictactoe-game/', include('tictactoe.urls')),
    path('url-shortener/', include('urlshortner.urls')),
    path('word-to-pdf/', include('wordtopdf.urls')),
    path('youtube-vedio-downloader/', include('yutubedownload.urls')),
    path("robots.txt",TemplateView.as_view(template_name="allok/robots.txt", content_type="text/plain")),
    path("sitemap.xml",TemplateView.as_view(template_name="allok/sitemap1.xml", content_type="text/plain")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

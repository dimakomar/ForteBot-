"""fortebot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from fortebot import views
import os

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^slack/', views.sent_message),
    url(r'^auth', views.auth),
    url(r'^temperature_vote', views.temperature_vote),
    url(r'^forte_vote', views.rating_vote),
    url(r'^anonymous_feedback/', views.anonymous_feedback),
    url(r'^anonymous_msg_random', views.anonymous_msg_random),
    url(r'^forte_help/', views.help),
    url(r'^get_results', views.get_results),
    url(r'^question_vote', views.start_question_vote),
    url(r'^delivery', views.delivery),
    url(r'^rate', views.rate),
]


"""vk_bot URL Configuration

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
from first_vk_bot import views
from django.urls import include

urlpatterns = [
    #url('auth', views.auth_, name='auth'),
    url('index', views.index, name='index'),
    url('send_message', views.send_message_, name='send_message'),
    url('invite', views.invite, name='invite'),
    url('signup', views.signup, name='signup'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]

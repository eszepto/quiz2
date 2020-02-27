"""s6101012620113 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from homepage import views as homepage_views
from calculator import views as post_views
from calculatorGET import views as get_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_views.main),
    path('aboutme/', homepage_views.aboutme, name='aboutme'),
    path('calculator/', post_views.main, name='calpost'),
    path('calculatorget/', get_views.main, name='calget'),
    path('api/cal/', post_views.calApi, name='calApi'),

]

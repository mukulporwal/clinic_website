"""
URL configuration for medical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.servicespage, name='services'),
    path('Blog/', views.Blog, name='Blog'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),
    path('gallery/', views.gallery, name='gallery'),
    path('fertility/<int:id>', views.fertility, name='fertility'),
    path('endometriosispage/<int:id>', views.endometriosispage, name='endometriosispage'),
    path('laparoscopypage/<int:id>', views.laparoscopypage, name='laparoscopypage'),
    path('riskdeliverypage/<int:id>', views.riskdeliverypage, name='riskdeliverypage'),
    path('blogdetail/<int:id>', views.blog_detail, name='blog_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about us/',views.about_us,name='about-us'),
    path('services/',views.services,name='services'),
    path('music/',views.music,name='music'),
    path('gallery/',views.gallery,name='gallery'),
    path('blog/',views.blog,name='blog'),
    path('blog/<int:pk>/',views.blog_detail,name='blog_detail'),
    path('contact/',views.contact,name='contact')
]

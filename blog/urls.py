from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="BlogHome"),
    path('about', views.about, name="about"),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
]

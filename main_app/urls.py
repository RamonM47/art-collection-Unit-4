from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('posts/', views.community_index, name='community_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about,name='about'),
    path('posts/', views.community_index, name='community_index'),
    path('posts/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:post_id>/add_worked_on/', views.add_worked_on, name ='add_worked_on'),
    path('posts/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'), #in this line we define the path for the index view
    path('list/', views.tweet_list, name='tweet_list'), #in thi line we define the parth for the tweet list view
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'), #in this line we define the path for the tweet edit view
    path('create/', views.tweet_create, name='tweet_create'), #in this line we define the part for the tweet create view
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'), # in this line we define the parth for the tweet delete view
    path('registerations/', views.register, name='register'), # in line we define the path for the register view
]
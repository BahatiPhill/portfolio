from django.urls import  path
from blog.views import blog, another_one,  article_details, edit_article

urlpatterns = [
    path('', blog, name='blog'),
    path('article/add/', another_one, name='another_one'),
    path('<slug:slug>/', article_details, name='article-details'),
    path('<slug:slug>/edit/', edit_article, name='article-edit'),
    
]
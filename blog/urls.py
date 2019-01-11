from django.urls import  path
from blog.views import blog, another_one, done, article_details

urlpatterns = [
    path('', blog, name='blog'),
    path('done/', done, name='done'),
    path('<slug:slug>/', article_details, name='article-details'),
    path('another_one/', another_one, name='another_one'),
]
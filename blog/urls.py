from django.urls import  path
from blog.views import index, another_one, done

urlpatterns = [
    path('', index, name='blog'),
    path('done/', done, name='done'),
    #path('<slug:title>/', article_details, name='article-detail'),
    path('another_one/', another_one, name='another_one'),
]
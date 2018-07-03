from django.urls import path
from blog import views


urlpatterns = [
    path('', views.index),
    path('category/<int:id>', views.category,name='category'),
    path('article_detail/<int:article_id>', views.article_detail,name='article_detail'),

]

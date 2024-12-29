from django.urls import path
from .import views

urlpatterns = [
   path('', views.news_home, name='news_file'),
   path('create/', views.create, name='create'),
   path('reg_user/', views.reg, name='register')

]
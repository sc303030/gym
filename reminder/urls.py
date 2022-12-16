from django.urls import path, include
from . import views
urlpatterns = [
    path('crawling/', views.crawling , name='crawling')
]
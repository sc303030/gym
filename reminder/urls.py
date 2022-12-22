from django.urls import path, include
from . import views

urlpatterns = [
    path('oauth/', views.oauth, name='oauth')
]

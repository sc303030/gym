from django.urls import include, path

from . import views

urlpatterns = [
    path('oauth/', views.oauth, name='oauth')
]

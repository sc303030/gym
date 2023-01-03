from django.urls import path

from . import views

urlpatterns = [path("oauth/", views.oauth, name="oauth")]

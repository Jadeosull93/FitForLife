from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # route and view, and name
]
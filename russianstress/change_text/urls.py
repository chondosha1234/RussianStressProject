from django.urls import path
from . import views

urlpatterns = [
    path('', views.change_text, name="change_text")
]

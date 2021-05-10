from django.urls import path
from homepage import views

urlpatterns = [
    # http//localhost:8000/homepage
    path('', views.home, name="home")
]
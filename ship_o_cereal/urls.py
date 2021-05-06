from django.urls import path
from ship_o_cereal import views

urlpatterns = [
    # http//localhost:8000
    path('', views.index, name="index"),
]
from django.urls import path
from ship_o_cereal import views

urlpatterns = [
    # http//localhost:8000
    path('', views.home, name="home"),
    path('store/', views.prod_view, name="ProductView")

]
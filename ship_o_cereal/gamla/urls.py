from django.urls import path
from store import views

urlpatterns = [
    # http//localhost:8000
    path('', views.index, name="index"),
    # http//localhost:8000/store

    #path('<int:id', views.get_product_by_id, name="product_details"),
    path('create_product', views.create_product, name="create_product")
]
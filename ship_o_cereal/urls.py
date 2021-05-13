from django.urls import path, re_path
from ship_o_cereal import views

urlpatterns = [
    path('', views.prod_view, name="ProductView"),
    path('popular/', views.popularitem, name="Popularitem"),
    path('<int:productId>', views.prod_by_id, name="ProductPage"),
    path('merch/',views.merch_view,name="MerchView"),
    path('bowl/',views.bowl_view,name="BowlView"),
    path('search/',views.searchbar,name="SearchBar"),
    path('<int:productId>/addtocart/', views.new_cart_test, name="addToCart"),
    path('popular/<int:productId>/addtocart', views.pop_cart, name="addToCart"),
    path('store/<int:productId>/addtocart', views.new_cart_test, name="addToCart")

]

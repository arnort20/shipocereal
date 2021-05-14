from django.urls import path, re_path
from ship_o_cereal import views



urlpatterns = [
    path('', views.prod_view, name="ProductView"),
    path('popular/', views.popularitem, name="Popularitem"),
    path('<int:productId>', views.prod_by_id, name="ProductPage"),
    path('merch/',views.merch_view,name="MerchView"),
    path('bowl/',views.bowl_view,name="BowlView"),
    path('spoon/',views.spoon_view,name="SpoonView"),
    path('mug/',views.mug_view,name="MugView"),
    path('tshirt/',views.tshirt_view,name="TShirtView"),
    path('milk/',views.milk_view,name="MilkView"),
    path('search/',views.searchbar,name="SearchBar"),
    path('<int:productId>/addtocart/', views.new_cart_test, name="addToCart"),
    path('popular/<int:productId>/addtocart', views.pop_cart, name="addToCart"),
    path('store/<int:productId>/addtocart', views.new_cart_test, name="addToCart"),
    path('bowl/<int:productId>/addtocart', views.merch_cart, name='addtocart'),
    path('mug/<int:productId>/addtocart', views.merch_cart, name='addtocart'),
    path('spoon/<int:productId>/addtocart', views.merch_cart, name='addtocart'),
    path('tshirt/<int:productId>/addtocart', views.merch_cart, name='addtocart'),
    path('milk/<int:productId>/addtocart', views.merch_cart, name='addtocart')

]

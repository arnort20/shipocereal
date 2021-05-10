from django.urls import path, re_path
from ship_o_cereal import views

urlpatterns = [
    # http//localhost:8000
    path('', views.home, name="home"),
    path('store/', views.prod_view, name="ProductView"),
    path('store/<int:productId>', views.prod_by_id, name="ProductPage"),
    path('merch/',views.merch_view,name="MerchView"),
    path('bowl/',views.bowl_view,name="BowlView"),
    path('cart/',views.cart_view,name="CartView"),
    path('checkout/',views.checkout_view,name="CheckoutView"),
    path('login/',views.login_view,name="LoginView"),
    path('signup/',views.signup_view,name="SignupView"),
    path('user/',views.user_view,name="UserView")
]

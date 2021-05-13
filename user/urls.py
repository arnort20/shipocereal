from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from user import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('cart/',views.cart_view,name="CartView"),
    path('checkout/',views.checkout_view,name="CheckoutView"),
    path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('signup/',views.signup_view,name="SignupView"),
    path('user/',views.user_view,name="UserView"),
    path('creditcard/',views.creditcard,name="CreditcardView"),
    path('address/', views.address, name="AddressView"),
    path('profile/',views.user_profile,name="userprofileView"),
    path('carttest/', views.new_cart_test,name="CartTest"),
]
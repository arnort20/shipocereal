from django.urls import path
from user import views


urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name='register'),
    path('cart/',views.cart_view,name="CartView"),
    path('checkout/',views.checkout_view,name="CheckoutView"),
    path('login/',views.login_view,name="LoginView"),
    path('signup/',views.signup_view,name="SignupView"),
    path('user/',views.user_view,name="UserView")
    # path('profile/')
]
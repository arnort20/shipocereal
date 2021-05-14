from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from user import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('cart/',views.cart_view,name="CartView"),
    path('cart/removeitem/<int:productId>',views.remove_from_cart,name="RemoveFromCart"),
    path('checkout/',views.checkout_view,name="CheckoutView"),
    path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',LogoutView.as_view(next_page='home'),name='logout'),
    path('signup/',views.signup_view,name="SignupView"),
    path('user/',views.user_view,name="UserView"),
    path('creditcard/',views.creditcard,name="CreditcardView"),
    path('address/', views.address, name="AddressView"),
    path('changePW/', views.Changepw_view, name="ChangepwView"),
    path('profile/',views.user_profile,name="userprofielView"),
    path('profile/updateUser',views.update_user_view,name="UpdateUser"),
    path('profile/updateProfile',views.update_profile_view,name="UpdateProfile"),
    path('carttest/', views.new_cart_test,name="CartTest"),
    path('checkout/address/', views.makeOrder,name="CheckoutAddress"),
    path('checkout/cart/', views.makeOrder,name="CheckoutCard"),
    path('checkout/makeorder/', views.makeOrder,name="ConfirmOrder")
]
from django.shortcuts import render
from ship_o_cereal.models import *


def prod_view(request):
    # allProducts = Products.objects.all()
    allProducts = {'products': Products.objects.all()}
    return render(request, 'store/store.html', context=allProducts)


def prod_by_id(request, productId):
    context = {'product': Products.objects.get(pk=productId)}
    return render(request, 'store/product_view.html', context=context)


def merch_view(request):
    return render(request, 'store/merch.html')


def bowl_view(request):
    return render(request, 'store/subcategory.html')


def cart_view(request):
    return render(request, 'store/../templates/user/cart.html')


def checkout_view(request):
    return render(request, 'store/../templates/user/checkout.html')


def login_view(request):
    return render(request, 'store/../templates/user/login.html')


def signup_view(request):
    return render(request, 'store/../templates/user/signup.html')


def user_view(request):
    return render(request, 'store/../templates/user/user.html')


def frontPage(request):
    return render(request, '')

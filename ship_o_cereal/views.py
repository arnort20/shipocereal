from django.shortcuts import render

def prod_view(request):
    return render(request, 'store/product_view.html')

def merch_view(request):
    return render(request, 'store/merch.html')

def bowl_view(request):
    return render(request, 'store/subcategory.html')

def cart_view(request):
    return render(request, 'store/cart.html')

def checkout_view(request):
    return render(request, 'store/checkout.html')

def login_view(request):
    return render(request, 'store/login.html')

def signup_view(request):
    return render(request, 'store/signup.html')

def user_view(request):
    return render(request, 'store/user.html')

def frontPage(request):
    return render(request, '')
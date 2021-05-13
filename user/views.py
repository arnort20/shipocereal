from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

import ship_o_cereal.models
from user.forms import credit_card_form, address_form, add_to_cart, add_to_cart_test
from user.forms import *
from user.forms.user_create_form import SignupForm
from django.contrib.auth import get_user_model
from ship_o_cereal.models import Carts, Orders, Addresses, CartRows, Creditcards, Comments
from user.models import Profile


from django.views.generic import ListView


def new_cart_test(request):
    if request.method == 'POST':
        print(1)
        form = add_to_cart_test.FolioCreateForm(data=request.POST)
        if form.is_valid():
            cart = form.save(commit=False)
            cart.userId_id = request.user.id
            cart.productId_id = request.productId
            cart = form.save()
    print(2)
    return render_to_response(request, 'user/new_cart_test.html', {
        'form': add_to_cart_test.FolioCreateForm()

    })


def cart_view(request):
    customer = request.user
    cart = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer)}
    return render(request, 'user/cart.html', context=cart)


def checkout_view(request):
    customer = request.user
    cart = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer)}
    return render(request, 'user/checkout.html', context=cart)


def signup_view(request):
    return render(request, 'user/signup.html')


def user_view(request):
    return render(request, 'user/../templates/store/user.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            print(1)
            return redirect('login')
        else:
            print(2)
    return render(request, 'user/register.html', {
        'form': SignupForm()
    })



def address(request):
    if request.method == 'POST':
        form = address_form.AddressCreateForm(data=request.POST)
        if form.is_valid:
            addr = form.save(commit=False)
            addr.userId_id = request.user.id
            addr = form.save()
            return redirect('userprofileView')
    else:
        form = address_form.AddressCreateForm()
    return render(request, 'user/address.html', {'form': form})



"""def address(request):
    if request.method == 'POST':
        form = drasl.CountrySelect(data=request.POST)
        if form.is_valid:
            addr = form.save()
            return redirect('userprofielView')
    else:
        form = drasl.CountrySelect()
    return render(request, 'user/address.html', {'form': form})"""




def addToCart(request, productId, amount):
    form = add_to_cart.AddToCart(data=request.POST)
    userId = request.user.id
    print(userId)
    if userId:
        currentCart = Carts.objects.get(userId_id=userId)
        if not currentCart:
            newCart(request, userId)
            currentCart = Carts.objects.get(userId_id=userId)
        print(cart_view(currentCart))
        cartRow = form.save(commit=False)
        cartRow.amount = amount
        cartRow.productId_id = productId
        cartRow.cartId_id = currentCart.cartId
        cartRow = form.save()
    print(productId)
    return render(request, 'store/add_to_cart.html', {'form': form})


def newCart(request, userId):
    form = add_to_cart.AddCart(data=request.POST)
    cart = form.save(commit=False)
    cart.userId_id = userId
    cart = form.save()



def creditcard(request):
    if request.method == 'POST':
        form = credit_card_form.CreditcardCreateForm(data=request.POST)
        if form.is_valid:
            card = form.save(commit=False)
            card.userId_id = request.user.id
            card = form.save()
            return redirect('userprofileView')
    else:
        form = credit_card_form.CreditcardCreateForm()
    return render(request, 'user/creditcard.html', {'form': form})

def user_profile(request):
    return render(request, 'user/profile.html')
#
#
# def profile(request):
#     profile = Profile.objects.filter(user=request.user).first()
#     if request.method == 'POST':
#         form = ProfileForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             return redirect('profile')
#     return render(request, 'user/profile.html', {
#         'form': ProfileForm(instance=profile)
#     })


















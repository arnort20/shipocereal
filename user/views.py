from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms import credit_card_form, address_form
from user.forms import *
from user.forms.user_create_form import SignupForm
from django.contrib.auth import get_user_model
from ship_o_cereal.models import Carts, Addresses, CartRows, Orders, Creditcards, Comments
from user.models import Profile


def cart_view(request):
    return render(request, 'user/cart.html')


def checkout_view(request):
    return render(request, 'user/checkout.html')

def signup_view(request):
    return render(request, 'user/signup.html')


def user_view(request):
    return render(request, 'user/../templates/store/user.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            return redirect('UserView')
    else:
        form = address_form.AddressCreateForm()
    return render(request, 'user/address.html', {'form': form})


def addToCart(request, productId, amount):
    form = add_to_cart.AddToCart(data=request.POST)
    userId = request.user.id
    if userId:
        currentCart = Carts.objects.get(userId_id=userId)
        if not currentCart:
            newCart(request, userId)
            currentCart = Carts.objects.get(userId_id=userId)
        cartRow = form.save(commit=False)
        cartRow.amount = amount
        cartRow.productId_id = productId
        cartRow.cartId_id = currentCart.cartId
        cartRow = form.save()


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


















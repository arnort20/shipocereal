from datetime import datetime

from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import ship_o_cereal.models
from user.forms import credit_card_form, address_form, add_to_cart, add_to_cart_test, user_update_info, profile_form
from user.forms import *
from user.forms.user_create_form import SignupForm
from django.contrib.auth import get_user_model
from ship_o_cereal.models import Carts, Orders, Addresses, CartRows, Creditcards, Comments,CartFolio
from user.models import Profile



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

def remove_from_cart(request,productId):
    cart = CartFolio.objects.filter(userId=request.user,productId=productId).first()
    cart.delete()
    return redirect('CartView')



def cart_view(request):
    customer = request.user
    cart_items = ship_o_cereal.models.CartFolio.objects.filter(userId=customer)
    if cart_items.exists():
        context = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer)}
    else:
        context = {'cart': ''}

    return render(request, 'user/cart.html', context=context)


def checkout_view(request):
    customer = request.user
    user_address = ship_o_cereal.models.Addresses.objects.filter(userId=customer).first()
    user_card = ship_o_cereal.models.Creditcards.objects.filter(userId=customer).first()
    if user_address:
        if user_card:
            context = {'user_address':user_address,
                       'user_card':user_card,
                       'customer':customer,
                       'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer)}
            if request.method == 'POST':
                makeOrder(request,user_address,user_card)
            return render(request, 'user/checkout_overview.html',context)
        else:
            return checkout_card(request)
    else:
        return checkout_address(request)

def checkout_address(request):
    if request.method == 'POST':
        form = address_form.AddressCreateForm(data=request.POST)
        if form.is_valid():
            new_address = form.save(commit=False)
            new_address.userId = request.user
            new_address.save()
            print('IM HERE')
            return checkout_view(request)

    user_address_form = address_form.AddressCreateForm()
    context = {'form':user_address_form}
    return render(request, 'user/checkout_address.html',context)

def checkout_card(request):
    if request.method == 'POST':
        form = credit_card_form.CreditcardCreateForm(data=request.POST)
        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.userId = request.user
            new_card.save()
            return redirect('CheckoutView')
    user_card_form = credit_card_form.CreditcardCreateForm()
    context = {'form':user_card_form}
    return render(request, 'user/checkout_card.html',context)


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
    address = Addresses.objects.filter(userId_id=request.user.id).first()
    if request.method == 'POST':
        form = address_form.AddressCreateForm(data=request.POST)
        if form.is_valid():
            if address:
                address.address = request.POST['address']
                apt_num = request.POST['apt_num']
                if apt_num == '':
                    address.apt_num = None
                else:
                    address.apt_num = int(apt_num)
                address.zip = request.POST['zip']
                address.country = request.POST['country']
                address.town = request.POST['town']
                address.save()
            else:
                new_address = form.save(commit=False)
                new_address.userId = request.user
                new_address.save()
            return redirect('AddressView')
    form = address_form.AddressCreateForm()
    context = {'form': form, 'address': address}
    return render(request, 'user/address.html', context)


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
    return render(request, 'store/add_to_cart.html', {'form': form})


def makeOrder(request,user_address,user_card):
    userId = request.user.id
    if userId:
        currentCart = CartFolio.objects.get(userId_id=userId)
        if not currentCart:
            return redirect('home')
        print(request.user.id)
        new_order = Orders()
        new_order.userId = request.user
        new_order.date = datetime.now()
        new_order.addrId_id = user_address.addrId
        new_order.cardId_id = user_card.cardId
        new_order.save()
        return redirect('home')
    return redirect('userprofielView')


def newCart(request, userId):
    form = add_to_cart.AddCart(data=request.POST)
    cart = form.save(commit=False)
    cart.userId_id = userId
    cart = form.save()



def creditcard(request,chekout=False):
    card = Creditcards.objects.filter(userId_id=request.user.id).first()
    if card:
        exp_date = "({}/{})".format(card.month, card.year)
        card_num = "****-****-****-"+card.cardNumber[12:]
        cardname = card.cardname
    else:
        card_num = ''
        exp_date = ''
        cardname = ''
    if request.method == 'POST':
        form = credit_card_form.CreditcardCreateForm(data=request.POST)
        if form.is_valid:
            if card:
                card = Creditcards.objects.filter(userId_id=request.user.id).first()
                card.cardname = request.POST['cardname']
                card.cardNumber = request.POST['cardNumber']
                card.month = request.POST['month']
                card.year = request.POST['year']
                card.cvc = request.POST['cvc']
                card.save()
            else:
                new_card = form.save(commit=False)
                new_card.userId = request.user
                new_card.save()
            return redirect('CreditcardView')

    form = credit_card_form.CreditcardCreateForm()
    context = {'form': form, 'card_num': card_num, 'name': cardname, 'exp_date': exp_date}
    return render(request, 'user/creditcard.html', context)


def user_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    updateUser_form = user_update_info.UpdateUserForm(instance=request.user)
    updateProfile_form = profile_form.ProfileForm(instance=profile)
    context = {'updateUser_form': updateUser_form, 'updateProfile_form':updateProfile_form}
    return render(request, 'user/profile.html', context)

def update_user_view(request):
    if request.method == 'POST':
        updateUser_form = user_update_info.UpdateUserForm(data=request.POST)
        if updateUser_form.is_valid():
            user = User.objects.filter(pk=request.user.id).first()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect('userprofielView')
    updateUser_form = user_update_info.UpdateUserForm(instance=request.user)
    context = {'updateUser_form':updateUser_form}
    return render(request, 'user/profile.html', context)

def update_profile_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        updateProfile_form = profile_form.ProfileForm(instance=profile, data=request.POST)
        if updateProfile_form.is_valid():
            profile = updateProfile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('userprofielView')
    context = {'updateProfile_form':profile_form.ProfileForm(instance=profile)}
    return render(request, 'user/profile.html', context)

def Changepw_view(request):
    if request.method == 'POST':
        changepw_form = PasswordChangeForm(request.user, data=request.POST)
        if changepw_form.is_valid():
            print(changepw_form.new_password)
            return redirect('ChangepwView')
    changepw_form = PasswordChangeForm(request.user)
    context = {'form': changepw_form}
    return render(request, 'user/changepw.html', context)














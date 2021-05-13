from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

import ship_o_cereal.models
from user.forms import credit_card_form, address_form, add_to_cart, add_to_cart_test, user_update_info, profile_form, order_form
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
    context = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer)}
    return render(request, 'user/cart.html', context=context)


def checkout_view(request):
    customer = request.user
    credits = ship_o_cereal.models.Creditcards.objects.filter(userId=customer)
    addressers = ship_o_cereal.models.Addresses.objects.filter(userId=customer)
    context = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer),
            'creditcards': credits[:1],
            'addresses': addressers[:1]}
    return render(request, 'user/checkout.html', context=context)


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
            return redirect('AddressView')
    form = address_form.AddressCreateForm()
    context = {'form': form, 'address': address}
    return render(request, 'user/address.html', context)


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


def makeOrder(request):
    form = order_form.OrderForm(data=request.POST)
    userId = request.user.id
    print(userId)
    if userId:
        currentCart = Carts.objects.get(userId_id=userId)
        if not currentCart:
            return redirect('home')
        print(cart_view(currentCart))
        theOrder = form.save(commit=False)
        theOrder.addrId = Addresses.objects.filter(userId=userId)
        theOrder.cardId = Creditcards.objects.filter(userId=userId)
        theOrder.userId = request.user
        theOrder.save()
    return redirect('userprofielView')


def newCart(request, userId):
    form = add_to_cart.AddCart(data=request.POST)
    cart = form.save(commit=False)
    cart.userId_id = userId
    cart = form.save()



def creditcard(request):
    card = Creditcards.objects.filter(userId_id=request.user.id).first()
    exp_date = "({}/{})".format(card.month,card.year)
    card_num = "****-****-****-"+card.cardNumber[12:]
    if request.method == 'POST':
        form = credit_card_form.CreditcardCreateForm(data=request.POST)
        if form.is_valid:
            card = Creditcards.objects.filter(userId_id=request.user.id).first()
            card.cardname = request.POST['cardname']
            card.cardNumber = request.POST['cardNumber']
            card.month = request.POST['month']
            card.year = request.POST['year']
            card.cvc = request.POST['cvc']
            card.save()
            return redirect('CreditcardView')

    form = credit_card_form.CreditcardCreateForm()
    context = {'form': form,'card_num':card_num,'name':card.cardname,'exp_date':exp_date}
    return render(request, 'user/creditcard.html',context)


def user_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    print(profile.profileImage)
    if request.method == 'POST':
        form = profile_form.ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('userprofielView')
    context = {'updateProfile_form':profile_form.ProfileForm(instance=profile),
               'profile':profile}

    return render(request, 'user/profile.html', context)

    """if request.method == 'POST':
        updateUser_form = user_update_info.UpdateUserForm(data=request.POST)
        if updateUser_form.is_valid():
            user = User.objects.filter(pk=request.user.id).first()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return redirect('userprofielView')
    else:
        updateUser_form = user_update_info.UpdateUserForm(instance=request.user)
    context = {'updateUser_form':updateUser_form}
    return render(request, 'user/profile.html',context)"""

"""def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
     if request.method == 'POST':
         form = ProfileForm(instance=profile, data=request.POST)
         if form.is_valid():
             profile = form.save(commit=False)
             profile.user = request.user
             profile.save()
             return redirect('profile')
     return render(request, 'user/profile.html', {
         'form': 
     })"""

















from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms import credit_card_form
from django.contrib.auth import get_user_model
from ship_o_cereal.models import Carts, Addresses, CartRows, Orders, Creditcards, Comments
from user.models import Profile


def cart_view(request):
    return render(request, 'user/cart.html')


def checkout_view(request):
    return render(request, 'user/checkout.html')


def login_view(request):
    return render(request, 'user/login.html')


def signup_view(request):
    return render(request, 'user/signup.html')


def user_view(request):
    return render(request, 'user/user.html')


def login(request):
    # if request.method == 'POST':
    #     form =
    return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def creditcard(request):
    if request.method == 'POST':
        form = credit_card_form.CreditcardCreateForm(data=request.POST)
        if form.is_valid:
            card = form.save(commit=False)
            card.userId_id = request.user.id
            print(card)
            print(request.user.id)
            card = form.save()
    else:
        form = credit_card_form.CreditcardCreateForm()
    return render(request, 'user/creditcard.html', {'form': form})
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


















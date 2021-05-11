from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm
from user.models import Profile


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


def login(request):
    return render(request, 'store/login.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'user/register.html', {
#         'form': UserCreationForm()
#     })
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


















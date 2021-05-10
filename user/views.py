from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'store/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

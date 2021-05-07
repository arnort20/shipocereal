from django.shortcuts import render


def home(request):
    return render(request, 'homepage/home.html')

def prod_view(request):
    return render(request, 'store/product_view.html')

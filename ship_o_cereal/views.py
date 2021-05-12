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


def frontPage(request):
    return render(request, '')


def searchbar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Products.objects.filter(name__contains=searched)
        return render(request, 'SearchSite.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'SearchSite.html')



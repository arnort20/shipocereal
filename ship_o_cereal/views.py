from django.shortcuts import render, redirect
from ship_o_cereal.models import *


def new_cart_test(request, productId):
    if not request.user.is_authenticated:
        return redirect('login')
    cartRelation = CartFolio.objects.filter(productId=Products.objects.filter(pk=productId).first(), userId=request.user)

    if not cartRelation:
        cart = CartFolio()
        cart.productId = Products.objects.filter(pk=productId).first()
        cart.userId = request.user
        cart.amount = 1
        cart.save()
    else:
        theCart = cartRelation.first()
        theCart.amount += 1
        theCart.save()
    return redirect('ProductView')

def pop_cart(request, productId):
    if not request.user.is_authenticated:
        return redirect('login')
    cartRelation = CartFolio.objects.filter(productId=Products.objects.filter(pk=productId).first(), userId=request.user)

    if not cartRelation:
        cart = CartFolio()
        cart.productId = Products.objects.filter(pk=productId).first()
        cart.userId = request.user
        cart.amount = 1
        cart.save()
    else:
        theCart = cartRelation.first()
        theCart.amount += 1
        theCart.save()
    return redirect('Popularitem')




def prod_view(request):
    # allProducts = Products.objects.all()
    allProducts = {'products': Products.objects.all()}
    return render(request, 'store/store.html', context=allProducts)

def popularitem(request):
    allProducts = {'product3': Products.objects.filter(pk=3), 'product4': Products.objects.filter(pk=4),
                   'product6': Products.objects.filter(pk=6), 'product11': Products.objects.filter(pk=11)}
    return render(request, 'store/popularitems.html', context=allProducts)


def prod_by_id(request, productId):
    context = {'product': Products.objects.get(pk=productId)}
    return render(request, 'store/product_view.html', context=context)


def merch_view(request):
    bowls = Products.objects.filter(typeId=2)
    spoons = Products.objects.filter(typeId=3)
    context = {'bowls': bowls[:5],
    'spoons': spoons[:5]}
    return render(request, 'store/merch.html', context=context)


def bowl_view(request):
    return render(request, 'store/subcategory.html')


def frontPage(request):
    return render(request, '')


def searchbar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Products.objects.filter(name__icontains=searched)
        return render(request, 'SearchSite.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'SearchSite.html')





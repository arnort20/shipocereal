from django.shortcuts import render, redirect,get_object_or_404
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

def merch_cart(request, productId):
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
    return redirect('MerchView')


def prod_view(request):
    # allProducts = Products.objects.all()
    allProducts = {'products': Products.objects.all()}
    return render(request, 'store/store.html', context=allProducts)

def popularitem(request):
    allProducts = {'product3': Products.objects.filter(pk=3), 'product4': Products.objects.filter(pk=4),
                   'product6': Products.objects.filter(pk=6), 'product11': Products.objects.filter(pk=11)}
    return render(request, 'store/popularitems.html', context=allProducts)


def prod_by_id(request,productId):
    #nutriens = Nutrients.objects.filter(pk=productId).first()
    context = {'product': Products.objects.get(pk=productId),
               'nutriens':Nutrients.objects.filter(pk=productId).first()}
    return render(request, 'store/product_view.html',context)


def merch_view(request):
    bowls = Products.objects.filter(typeId=2)
    spoons = Products.objects.filter(typeId=3)
    mugs = Products.objects.filter(typeId=4)
    tshirts = Products.objects.filter(typeId=5)
    milks = Products.objects.filter(typeId=6)
    context = {'bowls': bowls[:5], 'spoons': spoons[:5], 'mugs': mugs[:5], 'tshirts': tshirts[:5], 'milks': milks[:5]}
    return render(request, 'store/merch.html', context=context)


def bowl_view(request):
    bowls = Products.objects.filter(typeId=2)
    context = {'bowls': bowls[:5]}
    return render(request, 'store/subcategory.html', context=context)


def spoon_view(request):
    spoons = Products.objects.filter(typeId=3)
    context = {'spoons': spoons[:5]}
    return render(request, 'store/spoons.html', context=context)

def mug_view(request):
    mugs = Products.objects.filter(typeId=4)
    context = {'mugs': mugs[:5]}
    return render(request, 'store/mugs.html', context=context)

def tshirt_view(request):
    tshirts = Products.objects.filter(typeId=5)
    context = {'tshirts': tshirts[:5]}
    return render(request, 'store/tshirts.html', context=context)

def milk_view(request):
    milks = Products.objects.filter(typeId=6)
    context = {'milks': milks[:5]}
    return render(request, 'store/milks.html', context=context)

def frontPage(request):
    return render(request, '')


def searchbar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Products.objects.filter(name__icontains=searched)
        return render(request, 'SearchSite.html', {'searched': searched, 'products': products})
    else:
        return render(request, 'SearchSite.html')


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstimage': x.product.object.filter.first().image
        } for x in product.objects.filter(name__icontaints=search_filter) ]
        return jsonResponse({'data': products})
        context = {'products': product.objects.all().order_by('name')}
        return render(request, 'products/filter.html', context)




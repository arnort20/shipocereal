from django.shortcuts import render, redirect
# from forms.product_form import ProductModelFormset
from .product_form import ProductModelFormset


def index(request):
    return render(request, 'homepage/home.html')


def create_product(request):
    templateName = 'store/create_product.html'
    headingMessage = 'Model formset Demo'
    if request.method == 'GET':
        formset = ProductModelFormset(request.GET or None)
    elif request.method == 'POST':
        formset = ProductModelFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                # only save if name is present
                if form.cleaned_data.get('productName'):
                    form.save()
            return redirect('product_list')
        return render(request, templateName, {
            'formset': formset,
            'heading': headingMessage,
        })


    # if request.method == 'POST':
    #     print(1)
    # else:
    #     form =
    # return render(request, 'store/create_product.html', {
    #     'form': form
    # })


#
# def get_product_by_id(request, id):
#     return render(request, 'store/product.html', {
#         'product': get_object_or_404(Product, pk=id)
#     })


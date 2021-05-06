from django.forms import ModelForm, widgets, modelformset_factory
from django import forms

from .models import Products




ProductModelFormset = modelformset_factory(
    Products,
    exclude=['productId'],
    fields=(
        'name',
        'description',
        'typeId',
        'manId',
        'price',
        'image',
        'stock',
        'isFood'
    ),
    widgets = {
            'productName': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'typeId': widgets.Select(attrs={'class': 'form-control'}),
            'manId': widgets.Select(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'image': widgets.TextInput(attrs={'class': 'form-control'}),
            'stock': widgets.NumberInput(attrs={'class': 'form-control'}),
            'isFood': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }
)

# class ProductCreateForm(ModelForm):
#     image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = Products
#         exclude = ['productId']
#         widgets = {
#             'productName': widgets.TextInput(attrs={'class': 'form-control'}),
#             'description': widgets.TextInput(attrs={'class': 'form-control'}),
#             'typeId': widgets.Select(attrs={'class': 'form-control'}),
#             'manId': widgets.Select(attrs={'class': 'form-control'}),
#             'price': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'image': widgets.TextInput(attrs={'class': 'form-control'}),
#             'stock': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'isFood': widgets.CheckboxInput(attrs={'class': 'checkbox'})
#         }
#
#
# ProductFormset = formset_factory(ProductCreateForm, extra=1)

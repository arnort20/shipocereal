from django.forms import ModelForm, widgets
from ship_o_cereal.models import Carts, CartRows


class AddCart(ModelForm):
    class Meta:
        model = Carts
        exclude = ['cartId']


class AddToCart(ModelForm):
    class Meta:
        model = CartRows
        exclude = ['cartRowId']


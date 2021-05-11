from django.forms import ModelForm, widgets
from ship_o_cereal.models import Addresses


class AddressCreateForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['addrId', 'userId']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
        }

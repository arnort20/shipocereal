from django.forms import ModelForm, widgets
from ship_o_cereal.models import Addresses


class AddressCreateForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['addrId', 'userId']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control address__input'}),
            'apt_num': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
            'country': widgets.Select(attrs={'class': 'form-control address__input'})
        }



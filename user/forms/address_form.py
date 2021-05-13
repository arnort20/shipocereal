from django.forms import ModelForm, widgets
from ship_o_cereal.models import Addresses
from django_countries.widgets import CountrySelectWidget


class AddressCreateForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['addrId', 'userId','country']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control address__input'}),
            'apt_num': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
<<<<<<< HEAD
            #'country': widgets.Select(attrs={'class': 'form-control address__input'})
=======
            'country': CountrySelectWidget()
>>>>>>> 3fdc08a06f95d0204fb4205f8ea45ed7176dc539
        }



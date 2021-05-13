from django.forms import ModelForm, widgets
from ship_o_cereal.models import Addresses
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


class AddressCreateForm(ModelForm):
    country = CountryField(blank_label='Select a country').formfield(widget=CountrySelectWidget(attrs={"class": "form-control address__input"}))
    class Meta:
        model = Addresses
        exclude = ['addrId', 'userId']
        widgets = {
            'address': widgets.TextInput(attrs={'class': 'form-control address__input'}),
            'apt_num': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
            'zip': widgets.NumberInput(attrs={'class': 'form-control address__input-small'}),
            #'country' : CountrySelectWidget()
        }




from django.forms import ModelForm, widgets
from ship_o_cereal.models import Countries


class CountrySelect(ModelForm):
    class Meta:
        model = Countries
        exclude = ['countyId']
        widgets = {
            'country': widgets.Select(attrs={'class': 'form-control address__input'})
        }

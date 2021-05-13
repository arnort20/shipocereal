from django.forms import ModelForm, widgets
from ship_o_cereal.models import Creditcards
from django import forms



class CreditcardCreateForm(ModelForm):
    cardNumber = forms.CharField(max_length=16,min_length=16,
                                 widget= forms.TextInput(attrs={'class': 'form-control cardinfo__input'}))
    month = forms.IntegerField(max_value=12,min_value=1,
                               widget=forms.NumberInput(attrs={'class': 'form-control cardinfo__select cardinfo__month'}))
    year = forms.IntegerField(max_value=2030, min_value=2021,
                              widget=forms.NumberInput(attrs={'class': 'form-control cardinfo__select'}))
    cvc = forms.IntegerField(min_value=100, max_value=999,
                             widget=forms.NumberInput(attrs={'class': 'form-control cardinfo__select'}))
    class Meta:
        model = Creditcards
        exclude = ['cardId', 'userId']
        widgets = {
            'cardname': widgets.TextInput(attrs={'class': 'form-control cardinfo__input'})
        }


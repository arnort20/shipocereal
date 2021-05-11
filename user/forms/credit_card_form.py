from django.forms import ModelForm, widgets
from ship_o_cereal.models import Creditcards


class CreditcardCreateForm(ModelForm):
    class Meta:
        model = Creditcards
        exclude = ['cardId', 'userId']
        widgets = {
            'cardNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'month': widgets.NumberInput(attrs={'class': 'form-control'}),
            'year': widgets.NumberInput(attrs={'class': 'form-control'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control'}),
        }
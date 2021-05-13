from django.forms import ModelForm, widgets
from ship_o_cereal.models import Creditcards


class CreditcardCreateForm(ModelForm):
    class Meta:
        model = Creditcards
        exclude = ['cardId', 'userId']
        widgets = {
            'cardname': widgets.TextInput(attrs={'class': 'form-control cardinfo__input'}),
            'cardNumber': widgets.TextInput(attrs={'class': 'form-control cardinfo__input','onkeyup':'formatCreditCard()','maxlength':'10'}),
            'month': widgets.NumberInput(attrs={'class': 'form-control cardinfo__select cardinfo__month'}),
            'year': widgets.NumberInput(attrs={'class': 'form-control cardinfo__select'}),
            'cvc': widgets.NumberInput(attrs={'class': 'form-control cardinfo__select'}),
        }


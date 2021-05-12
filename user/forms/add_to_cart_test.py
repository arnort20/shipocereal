from django.forms import ModelForm, widgets
from ship_o_cereal.models import CartFolio


class FolioCreateForm(ModelForm):
    class Meta:
        model = CartFolio
        exclude = ['folioId']
        widgets = {
            'userId': widgets.NumberInput(attrs={'class': 'form-control'}),
            'productId': widgets.NumberInput(attrs={'class': 'form-control'}),
            'amount': widgets.NumberInput(attrs={'class': 'form-control'})
        }

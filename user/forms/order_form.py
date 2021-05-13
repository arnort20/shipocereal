from ship_o_cereal.models import Orders
from django.forms import ModelForm, widgets


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        exclude = ['orderId', 'userId', 'date']
        widgets = {
            'cardId': widgets.Select(attrs={'class': 'form-control'
                                            }),
            'addrId': widgets.Select(attrs={'class': 'form-control'
                                            })
        }

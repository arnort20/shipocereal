from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from ship_o_cereal.models import User

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model=User
        #firstname = User.first_name
        #lastname = 'HANNA'#User.last_name
        #email = 'ANNA'#User.email
        fields = ['first_name','last_name','email']
        widgets = {
            'first_name':widgets.TextInput(attrs={'class': 'form-control myinfo__input'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control myinfo__input'}),
            'email': widgets.TextInput(attrs={'class': 'form-control myinfo__input'})
        }


from django.forms import ModelForm, widgets
from django import forms
from ship_o_cereal.models import User

class UserCreateForm(forms.Form):
    class Meta:
        model = User
        exclude= {'id'}
        widgets ={
            'username': widgets.TextInput(attrs={'class':'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
            'confirm_password': widgets.TextInput(attrs={'class': 'form-control'})
        }
    #your_name = forms.CharField(label='Your name', max_length=100)
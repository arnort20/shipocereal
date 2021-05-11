from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from ship_o_cereal.models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        exclude = {'id'}
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        widgets = {
            'username' :widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Notendanafn'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Fyrra Nafn'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Eftir Nafn'}),
            'email': widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Netfang'}),
            'password1': widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Lykilorð'}),
            'password2': widgets.TextInput(attrs={'class': 'form-control signup__input','placeholder':'Staðfesta lykilorð'})
        }


"""
Required. 150 characters or fewer. Letters, digits and @/./+/-/_
Your password can’t be too similar to your other personal information.
Your password must contain at least 8 characters.
Your password can’t be a commonly used password.
Your password can’t be entirely numeric.
Enter the same password as before, for verification. """
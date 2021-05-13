
from collections import OrderedDict
from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import ugettext, ugettext_lazy as _


class PasswordChangeForm(SetPasswordForm):
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': ("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Gamla Lykilorðið"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control changepw__input'}))

    #new_password1 = forms.CharField(label=_("Nýja Lykilorðið"),
    #                               widget=forms.PasswordInput(attrs={'class':'form-control changepw__input'}))


    new_password2 = forms.CharField(label=_("Staðfesta nýja Lykilorðið"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control changepw__input'}))
    fields_order = [old_password,new_password2,]
    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password


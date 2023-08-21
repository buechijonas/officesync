from django import forms
from django.forms import ModelForm

from django.core.validators import MaxLengthValidator
import re


from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(ModelForm):
    first_name = forms.CharField(validators=[MaxLengthValidator(15)])
    last_name = forms.CharField(validators=[MaxLengthValidator(15)])
    username = forms.CharField(validators=[MaxLengthValidator(15)])
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]
        help_texts = {"username": ""}
        error_messages = {"name": {"required": "Pflichtfeld"}}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username ist ein Pflichtfeld")
        if " " in username:
            raise forms.ValidationError("Benutzername ist nur diese Format ist erlaubt 'vorname_nachname'. Daten von Majestic!")
        if not re.match("^[a-z0-9_.]+$", username):
            raise forms.ValidationError("Benutzername ist nur diese Format ist erlaubt 'vorname_nachname'. Daten von Majestic!")
        return username.lower()

    def save(self, commit=True):
        user = super().save(commit=commit)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

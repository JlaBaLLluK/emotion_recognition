from django.core.exceptions import ValidationError
from django.forms import Form, CharField, PasswordInput

from auth_user.models import AuthUser


class AuthorizationForm(Form):
    username = CharField(required=True, max_length=255)
    password = CharField(required=True, max_length=255, widget=PasswordInput)

    def clean(self):
        super().clean()
        user = AuthUser.objects.get(username=self.cleaned_data.get('username'))
        if not user.check_password(self.cleaned_data.get('password')):
            raise ValidationError({'password': ValidationError('This password is wrong!')})

        return self.cleaned_data

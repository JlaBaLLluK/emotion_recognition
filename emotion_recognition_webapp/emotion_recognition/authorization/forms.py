from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.forms import Form, CharField, PasswordInput

from auth_user.models import AuthUser


class AuthorizationForm(Form):
    username = CharField(required=True, max_length=255)
    password = CharField(required=True, max_length=255, widget=PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user = None
        try:
            user = AuthUser.objects.get(username=cleaned_data.get('username'))
        except ObjectDoesNotExist:
            raise ValidationError({'username': ValidationError('This username is wrong!')})

        if not user.check_password(cleaned_data.get('password')):
            raise ValidationError({'password': ValidationError('This password is wrong!')})

        return cleaned_data

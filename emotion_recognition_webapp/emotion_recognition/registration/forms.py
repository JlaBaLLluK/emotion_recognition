from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput, TextInput, EmailInput

user_model = get_user_model()


class RegistrationForm(ModelForm):
    password_confirm = CharField(required=True, max_length=255, widget=PasswordInput)

    class Meta:
        model = user_model
        fields = ['username', 'password', 'password_confirm']
        error_messages = {
            'username': {
                'unique': 'This username is already taken!',
            },
        }

    def clean(self):
        super().clean()
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirm'):
            raise ValidationError({'password_confirm': ValidationError("Passwords must be same!")})

        return self.cleaned_data

    def save(self, commit=True):
        user_model.objects.create_user(username=self.cleaned_data.get('username'),
                                       password=self.cleaned_data.get('password'))

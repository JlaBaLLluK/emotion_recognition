from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField, PasswordInput

user_model = get_user_model()


class EditProfileDataForm(ModelForm):
    class Meta:
        model = user_model
        fields = ['username', 'first_name', 'last_name']


class DeleteProfileForm(Form):
    password = CharField(required=True, widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(DeleteProfileForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        super().clean()
        password = self.cleaned_data.get('password')
        if not self.user.check_password(password):
            raise ValidationError('This password is wrong!')
        
        return password

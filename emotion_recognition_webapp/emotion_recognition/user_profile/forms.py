from django.contrib.auth import get_user_model
from django.forms import ModelForm

user_model = get_user_model()


class EditProfileDataForm(ModelForm):
    class Meta:
        model = user_model
        fields = ['username', 'first_name', 'last_name']

from django.core.validators import FileExtensionValidator
from django.forms import Form, FileField, FileInput


class ChooseFileForm(Form):
    file = FileField(required=True, validators=[FileExtensionValidator(['csv', ])], widget=FileInput(attrs={
        'class': 'file-upload',
        'id': 'file-upload'
    }))


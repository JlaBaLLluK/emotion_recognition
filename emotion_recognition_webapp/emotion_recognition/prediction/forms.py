from django.forms import FileInput, ModelForm

from prediction.models import Prediction


class ChooseFileForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['source_file', ]
        widgets = {
            'source_file': FileInput(attrs={'class': 'file-upload',
                                            'id': 'file-upload', }),
        }

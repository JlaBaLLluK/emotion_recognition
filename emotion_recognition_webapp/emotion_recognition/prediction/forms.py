from django.core.exceptions import ValidationError
from django.forms import FileInput, ModelForm

from prediction.models import Prediction
from pandas import read_csv


class ChooseFileForm(ModelForm):
    class Meta:
        model = Prediction
        fields = ['source_file', ]
        widgets = {
            'source_file': FileInput(attrs={'class': 'file-upload',
                                            'id': 'file-upload', }),
        }

    def clean_source_file(self):
        file = self.cleaned_data.get('source_file')
        data = read_csv(file)
        if 'pixels' not in data.columns:
            raise ValidationError('CSV file must contain "pixels" column.')

        for record in data.get('pixels'):
            if len(record.split()) != 48 * 48:
                raise ValidationError('Every record must contain 48*48 grayscale pixels, separated by spaces.')

        return file

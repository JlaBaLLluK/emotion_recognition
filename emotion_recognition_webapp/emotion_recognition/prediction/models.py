from django.core.validators import FileExtensionValidator
from django.db import models


class Prediction(models.Model):
    file = models.FileField(blank=False, validators=[FileExtensionValidator(['csv', ])], upload_to='csvs/')

    class Meta:
        db_table = 'Predictions'

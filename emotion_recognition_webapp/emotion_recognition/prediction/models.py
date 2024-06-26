from django.core.validators import FileExtensionValidator
from django.db import models


class Prediction(models.Model):
    source_file = models.FileField(blank=False, validators=[FileExtensionValidator(['csv', ])], upload_to='sources/')
    result_file = models.FileField(blank=True, upload_to='results/', default='', null=True)

    class Meta:
        db_table = 'Predictions'

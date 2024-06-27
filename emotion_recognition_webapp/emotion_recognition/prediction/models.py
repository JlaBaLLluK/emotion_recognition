from django.core.validators import FileExtensionValidator
from django.db import models

from auth_user.models import AuthUser


class Prediction(models.Model):
    source_file = models.FileField(blank=False, validators=[FileExtensionValidator(['csv', ])], upload_to='sources/')
    result_file = models.FileField(blank=True, upload_to='results/', default='', null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='predictions')

    class Meta:
        db_table = 'Predictions'

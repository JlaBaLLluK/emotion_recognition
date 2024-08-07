# Generated by Django 5.0.6 on 2024-07-02 13:41

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_prediction_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='result_file',
        ),
        migrations.AddField(
            model_name='prediction',
            name='result',
            field=models.CharField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='source_file',
            field=models.FileField(upload_to='sources/', validators=[django.core.validators.FileExtensionValidator(['png'])]),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-20 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='operations_done',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]

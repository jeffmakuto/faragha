# Generated by Django 5.0.6 on 2024-05-19 06:15

import django.core.validators
from django.db import migrations, models
from ilm.validators import MaxFileSizeValidator


class Migration(migrations.Migration):

    dependencies = [
        ('ilm', '0014_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('audio', 'Audio'), ('picture', 'Picture'), ('video', 'Video')], max_length=10),
        ),
        migrations.AlterField(
            model_name='content',
            name='file',
            field=models.FileField(upload_to='module_contents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png']), MaxFileSizeValidator(104857600)]),
        ),
        migrations.AlterUniqueTogether(
            name='content',
            unique_together={('module', 'title')},
        ),
    ]

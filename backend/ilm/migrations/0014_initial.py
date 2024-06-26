# Generated by Django 5.0.6 on 2024-05-19 04:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ilm', '0013_remove_module_course_delete_content_delete_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(1000)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilm.course')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video'), ('picture', 'Picture')], max_length=10)),
                ('file', models.FileField(upload_to='module_contents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'mov', 'avi', 'jpg', 'jpeg', 'png'])])),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ilm.module')),
            ],
        ),
    ]

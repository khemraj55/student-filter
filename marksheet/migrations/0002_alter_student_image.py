# Generated by Django 4.2.7 on 2023-11-01 13:41

from django.db import migrations, models
import marksheet.models


class Migration(migrations.Migration):

    dependencies = [
        ('marksheet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to=marksheet.models.upload_path_handler),
        ),
    ]
# Generated by Django 4.0.1 on 2023-04-21 09:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='some_slug', max_length=10, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
    ]

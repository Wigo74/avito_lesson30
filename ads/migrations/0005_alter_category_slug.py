# Generated by Django 4.0.1 on 2023-04-19 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_category_slug_alter_ad_description_alter_ad_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=10, validators=[django.core.validators.MaxLengthValidator(5)]),
        ),
    ]

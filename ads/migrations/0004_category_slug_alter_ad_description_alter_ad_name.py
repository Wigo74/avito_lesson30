# Generated by Django 4.0.1 on 2023-04-19 22:24

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='sume_slug', max_length=10, unique=True, validators=[django.core.validators.MaxLengthValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(10)]),
        ),
    ]

# Generated by Django 4.0.1 on 2023-04-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.1 on 2023-04-20 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]

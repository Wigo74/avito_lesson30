# Generated by Django 4.0.1 on 2023-04-21 09:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 21, 9, 22, 6, 709614, tzinfo=utc), validators=[users.validators.check_birth_date]),
        ),
    ]

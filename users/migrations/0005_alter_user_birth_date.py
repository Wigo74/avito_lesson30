# Generated by Django 4.0.1 on 2023-04-24 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_age_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 24, 18, 53, 28, 893204, tzinfo=utc), validators=[users.validators.check_birth_date]),
        ),
    ]

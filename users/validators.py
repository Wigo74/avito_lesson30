
from rest_framework.exceptions import ValidationError
import datetime


def check_birth_date(birth_date):
    today = datetime.date.today()
    age = (today.year - birth_date.year - 1) + ((today.month, today.day) >= (birth_date.month, birth_date.day))
    if age < 9:
        raise ValidationError(f"Возраст {age} меньше 9 лет")


def check_email(email):
    if "rambler" in email:
        raise ValidationError("С домена rambler регистрация запрещена")

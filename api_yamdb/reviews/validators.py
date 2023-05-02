import datetime as dt
from django.core.exceptions import ValidationError


def validate_year(val):
    current_year = dt.date.today().year
    if val > current_year:
        raise ValidationError(
            'Нельзя добавлять произведения, которые ещё не вышли!'
        )

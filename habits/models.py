from django.db import models

# Create your models here.
PERIOD = [
    ('EVERY DAY', 'раз в день'),
    ('EVERY WEEK', 'раз в неделю'),
    ('EVERY MONTH', 'раз в месяц'),
]

class Habit
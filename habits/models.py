from django.db import models

from users.models import NULLABLE, User

# Create your models here.
PERIOD = [
    ('EVERY DAY', 'раз в день'),
    ('EVERY WEEK', 'раз в неделю'),
    ('EVERY MONTH', 'раз в месяц'),
]

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки', **NULLABLE)
    #place = models.CharField(max_length=100, verbose_name='Место')
    #time = models.DateTimeField(verbose_name="время", **NULLABLE)
    #action = models.CharField(max_length=300, verbose_name="действие")
    #is_pleasant = models.BooleanField(default=True, verbose_name='Признак приятной привычки')

    #reward = models.CharField(verbose_name='вознаграждение', **NULLABLE)
    #related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)
    #is_published = models.BooleanField(default=True, verbose_name='Признак публичности привычки', **NULLABLE)

#Место — место, в котором необходимо выполнять привычку.
#Время — время, когда необходимо выполнять привычку.
#Действие — действие, которое представляет из себя привычка.
#Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
#Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
#Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
#Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
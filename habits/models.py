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
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.DateTimeField(verbose_name="Время", **NULLABLE)
    action = models.CharField(max_length=300, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=True, verbose_name='Признак приятной привычки')
    frequency = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность выполнения в днях')

    duration = models.DurationField(verbose_name='Продолжительность выполнения в минутах')

    reward = models.CharField(verbose_name='вознаграждение', **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Признак публичности привычки', **NULLABLE)
    execution_time = models.IntegerField(verbose_name='Время на выполнение')
    date = models.DateField(auto_now_add=True, verbose_name='Дата и время последней отправки')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return f'{self.action}, время: {self.time}, место: {self.place}'

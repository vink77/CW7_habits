from datetime import timedelta
from django.utils import timezone

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from school.models import Kurs, Subscription
from users.models import User


@shared_task
def kurs_update_info(kurs_id):
    kurs = Kurs.objects.get(pk=kurs_id)
    subscriptions = Subscription.objects.filter(course=kurs_id, is_active=True)
    for subscription in subscriptions:
        send_mail(subject=f'Обновление курса {kurs}',
                  message=f'Посмотрите новые материалы',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[subscription.user.email],
                  fail_silently=False)


@shared_task()
def user_activ():
    users = User.objects.all()
    for user in users:
        if user.last_login:
            if timezone.now() - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
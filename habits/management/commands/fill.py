from django.core.management.base import BaseCommand
import json
from users.models import User
class Command(BaseCommand):

    def handle(self, *args, **options):
        #Очищаем БД
        User.objects.all().delete()
        #Kurs.objects.all().delete()
        #Lesson.objects.all().delete()
        #Pay.objects.all().delete()


        with open('habits/data_json/data_users.json', 'r', encoding='UTF-8') as us:
            users_to_fill = json.load(us)
            for item in users_to_fill:
                User.objects.create(
                    pk=item['pk'],
                    email=item['fields']['email'],
                    phone=item['fields']['phone'],
                    city=item['fields']['city'],
                    avatar=item['fields']['avatar'],
                    is_staff=item['fields']['is_staff'],
                    is_superuser=item['fields']['is_superuser'],
                )



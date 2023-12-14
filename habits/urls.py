from django.urls import path

from habits.apps import HabitsConfig
from rest_framework.routers import DefaultRouter

from habits.views import HabitListAPIView, HabitPublicListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns =[
                 path("habits/", HabitListAPIView.as_view(), name="habits_list"),
                 path("habits/publiclist/", HabitPublicListAPIView.as_view(), name="habits_publiclist"),
                 path("habits/create/", HabitCreateAPIView.as_view(), name="habits_create"),
                 path("habits/<int:pk>/detail/", HabitRetrieveAPIView.as_view(), name="habits_detail"),
                 path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits_update"),
                 path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habits_delete"),

             ]
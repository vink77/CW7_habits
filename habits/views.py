from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.permissions import IsOwnerOrSuperuser
from habits.serializers import HabitSerializer, HabitPublicSerializer
from habits.paginators import HabitsPaginator

# Create your views here.


class HabitListAPIView(generics.ListAPIView):
    """Просмотр списка привычек"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrSuperuser]
    pagination_class = HabitsPaginator

    def get_queryset(self):
        # Показываем привычки текущего пользователя
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset

class HabitCreateAPIView(generics.CreateAPIView):
    """Cоздания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsOwnerOrSuperuser]

    def perform_create(self, serializer):
        # Присваеваем пользователя при создании привычки
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()

class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    queryset = Habit.objects.all()

class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    queryset = Habit.objects.all()

class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    queryset = Habit.objects.all()

class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр списка публичных привычек"""
    serializer_class = HabitPublicSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]
    pagination_class = HabitsPaginator
    queryset = Habit.objects.filter(is_public=True)


from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):

     class Meta:
        model = Habit
        fields = (
            'id', 'user', 'place', 'time', 'action', 'is_pleasant', 'related_habit', 'periodicity', 'reward',
            'duration', 'is_published', 'date')
        read_only_fields = ('user',)

class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('place', 'time', 'action', 'is_pleasant', 'periodicity', 'reward', 'is_pleasant')
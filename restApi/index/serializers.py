from rest_framework import serializers
from . import models

class FixedGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FixedGoal
        fields = ('id', 'image', 'tittle', 'subtitle')
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class FixedGoalViewset(viewsets.ModelViewSet):
    queryset = models.FixedGoal.objects.all()
    serializer_class = serializers.FixedGoalSerializer



# Create your views here.

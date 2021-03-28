from django.db import models
from django.db.models import fields
from rest_framework import serializers
from . import models 

class Questionserialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Questions
        fields= '__all__'

class Gradeserialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Grades
        fields='__all__'
    
class Fieldsserialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Fileds
        fields='__all__'

class Periodsserialaizer(serializers.ModelSerializer):
    class Meta:
        model= models.Periods
        fields='__all__'

class Choisesserialaizer(serializers.ModelSerializer):
    class Meta:
        model=models.Choises
        fields='__all__'

from django.http import request
from rest_framework import permissions, response, status, views, authentication, generics
from django.shortcuts import render
from . import serialaizers
from rest_framework import generics
from . import models 
from rest_framework import permissions
from rest_framework.settings import api_settings
from rest_framework.response import Response

class CreateQs(generics.CreateAPIView):
    serializer_class = serialaizers.Questionserialaizer
    permission_classes=[permissions.IsAdminUser,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class ListQs(generics.ListAPIView):
    queryset=models.Questions.objects.all()
    serializer_class = serialaizers.Questionserialaizer
    permission_classes=[permissions.IsAdminUser,]

class CreateFileds(generics.CreateAPIView):
    serializer_class= serialaizers.Fieldsserialaizer
    permission_classes=[permissions.IsAdminUser,]

class ListFields(generics.ListAPIView):
    queryset=models.Fileds.objects.all()
    serializer_class=serialaizers.Fieldsserialaizer
    permission_classes=[permissions.IsAdminUser,]

class CreateGrades(generics.CreateAPIView):
    serializer_class= serialaizers.Gradeserialaizer
    permission_classes=[permissions.IsAdminUser,]

class ListGrades(generics.ListAPIView):
    queryset=models.Grades.objects.all()
    serializer_class=[serialaizers.Gradeserialaizer]
    permission_classes=[permissions.IsAdminUser,]

class CreateOptions(generics.CreateAPIView):
    serializer_class= serialaizers.Choisesserialaizer
    permission_classes=[permissions.IsAdminUser,]

class ListOptions(generics.ListAPIView):
    queryset=models.Choises.objects.all()
    serializer_class= serialaizers.Choisesserialaizer
    permission_classes=[permissions.IsAdminUser]

class CreatePeriod(generics.CreateAPIView):
    serializer_class=[serialaizers.Periodsserialaizer]
    permission_classes=[permissions.IsAdminUser]

class ListPeriod(generics.ListAPIView):
    queryset=models.Periods.objects.all()
    serializer_class= serialaizers.Periodsserialaizer
    permission_classes=[permissions.IsAdminUser,]
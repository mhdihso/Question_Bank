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
        data=request.data
        type_qu=data.get('type_qu')
        choises=data.get('choices')
        answer_choice=data.get('answer_choice')
        if type_qu == "2":
            if choises == None or answer_choice==None:
                return Response ({"message":"ERROR"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        else:
            if choises != None or answer_choice!=None:
                return Response ({"message":"ERROR"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class ListQs(generics.ListAPIView):
    queryset=models.Questions.objects.all()
    serializer_class = serialaizers.Questionserialaizer
    permission_classes=[permissions.IsAdminUser,]

class DetailQs(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='id'
    queryset=models.Questions.objects.all()
    serializer_class= serialaizers.Choisesserialaizer
    permission_classes=[permissions.IsAdminUser]

class CreateOptions(generics.CreateAPIView):
    serializer_class= serialaizers.Choisesserialaizer
    permission_classes=[permissions.IsAdminUser,]

class DetailOptions(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='id'
    queryset=models.Choises.objects.all()
    serializer_class= serialaizers.Choisesserialaizer
    permission_classes=[permissions.IsAdminUser]

from django.shortcuts import render
from rest_framework import viewsets
from .models import language
from .serializers import LanguageSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = LanguageSerializer
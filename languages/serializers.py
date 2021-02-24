from rest_framework import serializers
from .models import language

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = language
        fields = ('id', 'url', 'name', 'paradigm')
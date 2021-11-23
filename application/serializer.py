from rest_framework import serializers
from .models import application

class applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = application
        fields = ('title', 'application_feedback',  'description', 'author')
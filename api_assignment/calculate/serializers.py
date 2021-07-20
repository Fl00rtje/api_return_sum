from rest_framework import serializers
from .models import Number


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = ['id', 'num_1', 'num_2', 'total']
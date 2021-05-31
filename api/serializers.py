from rest_framework import serializers
from .models import Operation


class ArgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['arg1', 'arg2']


class ArgAndOpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['arg1', 'arg2', 'operation_name']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['result']


class OperationSerializer(serializers.ModelSerializer):
    performed = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Operation
        fields = '__all__'

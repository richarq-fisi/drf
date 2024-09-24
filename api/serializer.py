from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        # fields = ('fullname', 'nickname')
        fields = '__all__'

from rest_framework import serializers
from app.models import Parcela

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parcela
        fields = '__all__'


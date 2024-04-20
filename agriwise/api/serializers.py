from rest_framework import serializers
from app.models import Parcela, Registo

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        #fields = '__all__'
        exclude = ['user']

class RegistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registo
        fields = '__all__'

class ParcelaDetailSerializer(serializers.ModelSerializer):
    registos = RegistoSerializer(many=True, read_only=True)
    class Meta:
        model = Parcela
        fields = ['id','nome', 'area', 'registos']





# COLOCAR OS REGISTOS #
class RegistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registo
        exclude = ['parcela']

class RegistoDetailSerializer(serializers.ModelSerializer):
    registos = RegistoSerializer(many=True, read_only=True)
    class Meta:
        model = Registo
        fields = ['id','data','produto','dose','registos']


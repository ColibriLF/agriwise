from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Parcela, Registo
from .serializers import ParcelaSerializer


class ListPARCELAS(APIView):
    """List all todas as Parcelas"""

    def get(self, request):
        parcelas = Parcela.objects.all()
        serializer = ParcelaSerializer(parcelas, many=True)
        return Response(serializer.data)

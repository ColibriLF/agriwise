from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Parcela, Registo
from .serializers import ParcelaSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class ListPARCELAS(APIView):
    """List all todas as Parcelas"""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        parcelas = Parcela.objects.filter(user=request.user)
        serializer = ParcelaSerializer(parcelas, many=True)
        return Response(serializer.data)

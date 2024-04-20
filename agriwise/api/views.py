from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from rest_framework.response import Response
from app.models import Parcela, Registo
from .serializers import ParcelaSerializer, ParcelaDetailSerializer

class ListPARCELAS(APIView):
    """List all todas as Parcelas"""


    def get(self, request):
        parcelas = Parcela.objects.filter(user=request.user)
        serializer = ParcelaSerializer(parcelas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParcelaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailPARCELAS(APIView):


    def get(self, request, parcelas_id):
        parcela = get_object_or_404(Parcela, pk=parcelas_id, user=request.user)
        serializer = ParcelaDetailSerializer(parcela, many=False)
        return Response(serializer.data)

    def delete(self,request, parcelas_id):
        parcela = get_object_or_404(Parcela, pk=parcelas_id, user=request.user)
        parcela.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self,request, parcelas_id):
        parcela = get_object_or_404(Parcela, pk=parcelas_id, user=request.user)
        serializer = ParcelaDetailSerializer(parcela, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

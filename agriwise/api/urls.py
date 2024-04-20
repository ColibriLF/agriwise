from django.urls import path
from . import views

urlpatterns = [
    path('parcelas/', views.ListPARCELAS.as_view()),
    path('parcelas/<int:parcelas_id>/', views.DetailPARCELAS.as_view())

]
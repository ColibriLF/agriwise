from django.urls import path
from . import views

urlpatterns = [
    path('parcelas/', views.ListPARCELAS.as_view()),
    path('parcelas/<int:parcelas_id>/', views.DetailPARCELAS.as_view()),
# COLOCAR OS REGISTOS #
    path('parcelas/<int:parcelas_id>/registos/', views.ListREGISTOS.as_view()),
    path('parcelas/<int:parcelas_id>/registos/<int:registos_id>/', views.DetailREGISTOS.as_view()),

]
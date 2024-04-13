from django.urls import path
from . import views
from .models import Parcela

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('parcelas/<int:parcelas_id>/', views.parcelas_list, name='parcelas_list'),
    path('registo/<int:registo_id>/add/', views.add_data, name='add_data'),
    path('registo/<int:registo_id>/add/', views.add_produto, name='add_produto'),
    path('registo/<int:registo_id>/add/', views.add_dose, name='add_dose'),
]

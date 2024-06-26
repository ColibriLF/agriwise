from django.urls import path
from . import views
from .models import Parcela, Registo

urlpatterns = [
    path('', views.index, name='app_index'),
    path('login/', views.app_login, name='app_login'),
    path('logout/', views.app_logout, name='app_logout'),
    path('parcelas/<int:parcelas_id>/', views.parcelas_list, name='parcelas_list'),
    path('parcelas/<int:parcela_id>/addregisto/', views.add_produto_dose, name='add_produto_dose'),
    path('parcelas/addparcela/', views.add_parcela, name='add_parcela'),
    path('parcelas/', views.add_parcela, name='add_parcela'),
    path('parcelas/removeregisto/<int:registos_id>/', views.remove_registo, name='remove_registo'),
    path('parcelas/removeparcela/<int:parcelas_id>/', views.remove_parcela, name='remove_parcela'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.ListTODOS.as_view()),
    path('lists/<int:list_id>/', views.DetailTODOS.as_view())



]
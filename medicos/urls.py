from django.urls import path
from .views import medicos_list, medicos_create, medicos_update, medicos_delete, grafico_sueldos_medicos

urlpatterns = [
path('create/', medicos_create, name='medicos_create'),
path('', medicos_list, name='medicos_list'),
path('update/<int:id>/', medicos_update, name='medicos_update'),
path('delete/<int:id>/', medicos_delete, name='medicos_delete'),
path('sueldos/', grafico_sueldos_medicos, name='grafico_sueldos_medicos'),
]
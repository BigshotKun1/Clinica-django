from django.urls import path
from .views import pacientes_list, pacientes_create, pacientes_update, pacientes_delete

urlpatterns = [
path('create/', pacientes_create, name='pacientes_create'),
path('', pacientes_list, name='paciente_list'),
path('update/<int:id_paciente>/', pacientes_update, name='pacientes_update'),
path('delete/<int:id_paciente>/', pacientes_delete, name='pacientes_delete'),
]
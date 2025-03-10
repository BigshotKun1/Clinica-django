from django.urls import path     
from .views import certificados_list, certificados_create, certificados_update, generar_certificado
from . import views

urlpatterns = [
    path('', certificados_list, name='certificados_list'),
    path('create/', certificados_create, name='certificados_create'),
    path('update/<int:id_certificado>/', certificados_update, name='certificados_update'),
    path('certificado/<int:certificado_id>/', views.generar_certificado, name='generar_certificado'),
]
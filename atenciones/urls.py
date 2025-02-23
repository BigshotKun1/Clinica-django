from django.urls import path
from .views import atenciones_list, atenciones_create, atenciones_update

urlpatterns = [
    path('', atenciones_list, name='atenciones_list'),
    path('create/', atenciones_create, name='atenciones_create'),
    path('update/<int:id_atencion>/', atenciones_update, name= 'atenciones_update'),
]
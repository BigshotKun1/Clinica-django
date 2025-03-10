from django.urls import path
from .views import login_view, logout_view, registro_usuario, usuario_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('', usuario_list, name='usuario_list'),
]
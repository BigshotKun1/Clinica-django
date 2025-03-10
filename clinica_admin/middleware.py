from django.shortcuts import redirect
from django.urls import reverse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and hasattr(request.user, 'rol'):
            rutas_por_rol = {
                'admin': reverse('home'),
                'medico': reverse('home'),
                'paciente': reverse('home'),
            }

            ruta_actual = request.path
            ruta_destino = rutas_por_rol.get(request.user.rol)

            if ruta_destino and ruta_actual != ruta_destino:
                return redirect(ruta_destino)

        return self.get_response(request)

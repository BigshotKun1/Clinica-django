from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario 
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['clave']) 
            usuario.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
            
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro_usuario.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()

        if email and password:
            User = get_user_model()
            try:
                user = User.objects.get(email=email)  
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Inicio de sesión exitoso.")
                    return redirect("home")
                else:
                    messages.error(request, "Contraseña incorrecta.")  
            except User.DoesNotExist:
                messages.error(request, "El usuario con este correo no existe.")  
        else:
            messages.error(request, "Por favor, completa todos los campos.")

    return render(request, "usuarios/login.html")

@login_required
def logout_view(request):
    storage = get_messages(request)
    for _ in storage:  
        pass

    logout(request)
    messages.success(request, "Cierre de sesión exitoso.")
    return redirect("login")

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/list.html', {'usuarios': usuarios})
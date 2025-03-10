from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm, PacienteFormEdit
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def pacientes_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/list.html', {'pacientes': pacientes})

@login_required
def pacientes_create(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/form.html', {'form': form})

@login_required
def pacientes_delete(request, id_paciente):
    pacientes = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == "POST":
        pacientes.delete()
        return redirect('paciente_list')
    return render(request, 'pacientes/delete.html', {'pacientes': pacientes})

# Editar persona
@login_required
def pacientes_update(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == "POST":
        form = PacienteFormEdit(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteFormEdit(instance=paciente)
    return render(request, 'pacientes/form.html', {'form': form})

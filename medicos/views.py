from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def medicos_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/list.html', {'medicos': medicos})

@login_required
def medicos_create(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            medico = form.save()  # Guardamos el médico creado
            return redirect('medicos_list')
    else:
        form = MedicoForm()

    # Filtramos solo los usuarios con rol 'medico'
    usuarios_medicos = Usuario.objects.filter(rol='medico')

    context = {
        'form': form,
        'usuarios_medicos': usuarios_medicos,  # Pasamos los usuarios con rol 'medico'
    }

    return render(request, 'medicos/form.html', context)

@login_required
def medicos_delete(request, id):
    medicos = get_object_or_404(Medico, id=id)
    if request.method == "POST":
        medicos.delete()
        return redirect('medicos_list')
    return render(request, 'medicos/delete.html', {'medicos': medicos})

@login_required
def medicos_update(request, id):
    medico = get_object_or_404(Medico, id=id)
    if request.method == "POST":
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medicos_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'medicos/form.html', {'form': form})

@login_required
def grafico_sueldos_medicos(request):
    
    medicos = Medico.objects.all()
    #lista 
    nombres_medicos = []
    sueldos = []

    #lista atención
    atenciones_realizadas = []

    # Recorrer los médicos
    for medico in medicos:
        nombres_medicos.append(f"{medico.nombre} {medico.apellido}")
        sueldos.append(medico.sueldo) 
        atenciones_realizadas.append(medico.atencion_set.count()) 

    context = {
        'nombres_medicos': nombres_medicos,
        'sueldos': sueldos,
        'atenciones_realizadas': atenciones_realizadas,
    }
    return render(request, 'clinica_admin/base.html', context)
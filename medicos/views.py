from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico
from .forms import MedicoForm


# Create your views here.
def medicos_list(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos/list.html', {'medicos': medicos})

def medicos_create(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicos_list')
    else:
        form = MedicoForm()
    return render(request, 'medicos/form.html', {'form': form})

def medicos_delete(request, id):
    medicos = get_object_or_404(Medico, id=id)
    if request.method == "POST":
        medicos.delete()
        return redirect('medicos_list')
    return render(request, 'medicos/delete.html', {'medicos': medicos})


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

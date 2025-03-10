from django.shortcuts import render
from .models import Atencion
from .forms import AtencionForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def atenciones_list(request):
    atenciones = Atencion.objects.all()
    return render(request, 'atenciones/list.html', {'atenciones': atenciones}) 

@login_required
def atenciones_create(request):
    if request.method == "POST":
        form = AtencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atenciones_list')
    else:
        form = AtencionForm()
    return render(request, 'atenciones/form.html', {'form': form})

@login_required
def atenciones_update(request, id_atencion):
    atencion = Atencion.objects.get(id_atencion=id_atencion)
    if request.method == "POST":
        form = AtencionForm(request.POST, instance=atencion)
        if form.is_valid():
            form.save()
            return redirect('atenciones_list')
    else:
        form = AtencionForm(instance=atencion)
    return render(request, 'atenciones/form.html', {'form': form})

@login_required
def atenciones_delete(request, id_atencion):
    atencion = get_object_or_404(Atencion, id_atencion=id_atencion)
    if request.method == "POST":
        atencion.delete()
        return redirect('atenciones_list')
    return render(request, 'atenciones/delete.html', {'atencion': atencion})


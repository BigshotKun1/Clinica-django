from django.shortcuts import render
from .models import Certificado
from .forms import CertificadoForm
from django.shortcuts import redirect

# Create your views here.

def certificados_list(request):
    certificados = Certificado.objects.all()
    return render(request, 'certificados/list.html', {'certificados': certificados})

def certificados_create(request):
    if request.method == "POST":
        form = CertificadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificados_list')
    else:
        form = CertificadoForm()
    return render(request, 'certificados/form.html', {'form': form})

def certificados_update(request, id_certificado):
    certificado = Certificado.objects.get(id_certificado=id_certificado)
    if request.method == "POST":
        form = CertificadoForm(request.POST, instance=certificado)
        if form.is_valid():
            form.save()
            return redirect('certificados_list')
    else:
        form = CertificadoForm(instance=certificado)
    return render(request, 'certificados/form.html', {'form': form})
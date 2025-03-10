from django.shortcuts import render
from .models import Certificado
from .forms import CertificadoForm
from django.shortcuts import redirect
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.contrib.staticfiles import finders
from django.contrib.auth.decorators import login_required

@login_required
def certificados_list(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.rol == 'medico':
            certificados = Certificado.objects.all() 
        else:
            certificados = Certificado.objects.filter(id_atencion__id_paciente=request.user.paciente)
        return render(request, 'certificados/list.html', {'certificados': certificados})



@login_required
def certificados_create(request):
    if request.method == "POST":
        form = CertificadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificados_list')
    else:
        form = CertificadoForm()
    return render(request, 'certificados/form.html', {'form': form})

@login_required
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


@login_required
def generar_certificado(request, certificado_id):
    certificado = Certificado.objects.get(id_certificado=certificado_id)
    atencion = certificado.id_atencion

    # Configuración de la respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=certificado_{certificado_id}.pdf'

    # Crear el canvas para el PDF
    c = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Logo de la clínica (si tienes uno)
    logo_path = finders.find("escudo-color-gradiente.png")
    c.drawImage(logo_path, 30, height - 70, width=100, height=50)

    # Título del Certificado
    c.setFont("Helvetica-Bold", 30)
    c.drawString(150, height - 100, "CERTIFICADO MÉDICO")

    # Línea separadora
    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.line(30, height - 110, width - 30, height - 110)

    # Espaciado entre elementos
    y_position = height - 150

    # Datos del paciente
    c.setFont("Helvetica", 12)
    c.drawString(100, y_position, f"Paciente: {atencion.id_paciente.nombre} {atencion.id_paciente.apellido}")
    y_position -= 20
    c.drawString(100, y_position, f"Fecha de emisión: {certificado.fecha_emision.strftime('%d/%m/%Y')}")
    y_position -= 20
    c.drawString(100, y_position, f"Medico: {atencion.id_medico.nombre} {atencion.id_medico.apellido}")
    y_position -= 20
    c.drawString(100, y_position, f"Especialidad: {atencion.id_medico.especialidad}")
    y_position -= 30

    # Descripción del certificado
    c.drawString(100, y_position, "Descripción:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    c.drawString(100, y_position, f"{certificado.descripcion}")
    y_position -= 40

    # Firma
    c.setFont("Helvetica", 12)
    c.drawString(100, y_position, "Firma del Médico:")
    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position, f"Dr. {atencion.id_medico.nombre} {atencion.id_medico.apellido}")

    # Línea para firma
    y_position -= 10
    c.line(100, y_position, width - 100, y_position)

    # Pie de página 
    c.setFont("Helvetica", 8)
    c.drawString(100, 30, "Este certificado es válido únicamente con la firma del médico.")
    c.drawString(100, 15, "Clinica UBB | Avda. Collao 1202 Casilla 5-C, Concepción, Bío Bío | Teléfono: 123-456-7890")

    # Finalizar el PDF
    c.showPage()
    c.save()

    return response
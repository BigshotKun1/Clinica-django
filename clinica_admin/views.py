from django.shortcuts import render

def home (request):
    return render(request, 'clinica_admin/base.html')

def staff (request):
    return render(request, 'clinica_admin/staff.html')
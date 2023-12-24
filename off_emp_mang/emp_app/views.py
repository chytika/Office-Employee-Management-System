from django.shortcuts import render
from .models import employee, Role, Department

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = employee.objects.all()
    
    context = {
        'emps': emps
    }

    print(context)
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    return render(request, '')

def remove_emp(request):
    return render(request, '')

def filter_emp(request):
    return render(request, '')


from django.shortcuts import render, HttpResponse
from .models import employee, Role, Department
from datetime import datetime
from django.db.models import Q


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
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name  = request.POST['last_name']
    dept  = int(request.POST['dept'])
    salary  = int(request.POST['salary'])
    bonus  =int(request.POST['bonus'])
    role  = int(request.POST['role'])
    phone  = int(request.POST['phone'])
    # hire_date = int(request.POST['hire_date'])
    new_emp = employee(first_name=first_name, last_name=last_name, dept_id= dept, salary=salary, bonus=bonus, role_id= role, phone=phone,
                       hire_date=datetime.now())
    new_emp.save()
    return HttpResponse("Employee Added Successfully",)
    
  elif request.method == "GET":
    return render(request, 'add_emp.html')
  else:
    return HttpResponse("An Expection occured! Employee Has Not Been Added")
  

def remove_emp(request, emp_id = 0):
     if emp_id:
        try:
           emp_to_be_removed = employee.objects.get(id=emp_id)
           emp_to_be_removed.delete()

           return HttpResponse("Emploee Removed Successfully")
        
        except:
           return HttpResponse("Pls Enter a valid id")
        
     emps = employee.objects.all()
    
     Data = {
        'emps': emps
     }

     print(Data)
     return render(request, 'remove_emp.html', Data)


def filter_emp(request):
    if request.method == "POST":
       name = request.POST['name']
       dept = request.POST['dept']
       role = request.POST['role']
       emps = employee.objects.all()
       if name:
          emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

       if dept:
          emps = emps.filter(dept__name__icontains = dept)
          
       if role:
            emps = emps.filter(role__name__icontains = role)

            context = {
            'emps': emps
             }
            
            return render(request, 'view_all_emp.html', context)
    
    elif request.method == "GET":
      return render(request, 'filter_emp.html')
    else:
     return HttpResponse("Exceptional Occured!")



    
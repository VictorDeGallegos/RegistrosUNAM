from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import employeeForm
from .models import employee
from django.http import HttpResponseRedirect
# Create your views here.


@login_required
def employee_list(request):
    employees = employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})


@login_required
def employee_form(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            newUser = employee(
                nombre_completo=request.POST['nombre_completo'],
                CURP=request.POST['CURP'],
                direccion=request.POST['direccion'],
                sueldo=request.POST['sueldo'],
                numero_de_empleado=request.POST['numero_de_empleado'],
                antiguedad=request.POST['antiguedad'],
                position=form.cleaned_data['position']

            )
            newUser.save()
            return redirect('/registro')
    else:
        form = employeeForm()
    context = {'form': form}

    return render(request, 'employee/employeeform.html', context)


@login_required
def employee_delete(request, id):
    emp = employee.objects.get(pk=id)
    emp.delete()
    return redirect('/registro')


@login_required
def employee_update(request, id):
    if request.method == 'POST':
        pi = employee.objects.get(pk=id)
        fm = employeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = employee.objects.get(pk=id)
        fm = employeeForm(instance=pi)

    return render(request, 'employee/employeeUpdate.html', {'form': fm})

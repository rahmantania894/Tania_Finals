from tkinter.font import names

from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render, redirect

from employee.models import Employee

def employees(request):
   result = Employee.objects.all()
   return render(request, 'employees.html', {'result': result})

def new_employee(request):
   #print(request.POST)
   if request.method == 'POST':
      try:
         name = request.POST['name']
         email = request.POST['email']
         age = request.POST['age']
         phone_number = request.POST['phone_number']
         address = request.POST['address']
         department = request.POST['department']
         salary = request.POST['salary']
         print(f"Name: {name}, Email: {email}, Age: {age}, Phone Number: {phone_number}, Address: {address}, Department: {department}, Salary {salary}")
         Employee.objects.create(name=name, email=email, age=age, phone_number=phone_number, address=address,
         department=department, salary=salary)
      except Exception as e:
         print(e)
      return redirect("employees")
   return render(request, 'new_employee.html')

def update_employee(request, id):
   employee = Employee.objects.get(id=id)
   if request.method == 'POST':
      employee.name = request.POST['name']
      employee.email = request.POST['email']
      employee.age = request.POST['age']
      employee.phone_number = request.POST['phone_number']
      employee.address = request.POST['address']
      employee.department = request.POST['department']
      employee.salary = request.POST['salary']
      employee.save()
      return redirect("employees")

   return render(request, 'update_employee.html', {'employee': employee})


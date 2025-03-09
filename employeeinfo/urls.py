"""
URL configuration for employeeinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from employee.views import employees, new_employee, update_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    #Get All Employees
    path('employees/', employees, name= "employees"),
    #Create New Employee
    path("employees/new/", new_employee, name= "new_employee"),
    #Update Employees
    path("employees/update/<int:id>/", update_employee, name= "update_employee")
]

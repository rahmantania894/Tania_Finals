from django.db import models

class Employee(models.Model):
    #objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

   # def __str__(self):
#        return self.name

    class Meta:
        db_table = 'employees'
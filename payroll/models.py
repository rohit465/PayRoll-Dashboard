from django.db import models

class Employee(models.Model):
    emp_no = models.IntegerField(primary_key=True)
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Employee {self.emp_no}"

class Attendance(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    days_present = models.IntegerField()

    def __str__(self):
        return f"Employee {self.emp_no.emp_no} - {self.month}"

class IncomeTax(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Employee {self.emp_no.emp_no} - IT {self.tax_percentage}%"

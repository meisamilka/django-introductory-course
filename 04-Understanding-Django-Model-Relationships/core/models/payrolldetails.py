from django.db import models
from .employee import Employee


# class PayrollDetails(models.Model):
#     employee = models.OneToOneField(
#         Employee, on_delete=models.PROTECT)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateField()

#     def __str__(self):
#         return f"{self.employee.name} - {self.payment_date}"


# class PayrollDetails(models.Model):
#     employee = models.ForeignKey(
#         Employee, on_delete=models.PROTECT, null=True, blank=True, unique=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateField()

#     def __str__(self):
#         return f"{self.employee.name} - {self.payment_date}"

    
class PayrollDetails(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, unique=True, primary_key=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.payment_date}"

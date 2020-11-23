from django.db import models


class Employee(models.Model):
    cname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    clg_name = models.CharField(max_length=100)
    transport = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"



class candidatedb(models.Model):
      Technology=models.CharField(max_length=100)
      Experience=models.CharField(max_length=100)
      Job_Location=models.CharField(max_length=100)
      Passed_out=models.CharField(max_length=10)
      expected_monthly_salary=models.CharField(max_length=10)
      Past_company=models.CharField(max_length=20)
      Reference=models.CharField(max_length=50)
      course_fees=models.CharField(max_length=20)

      class Meta:
          db_table='candidate'






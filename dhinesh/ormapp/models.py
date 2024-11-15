from django.db import models
from django.contrib import admin
class Loan(models.Model):
   lid=models.CharField(max_length=15,primary_key="lid")
   loantype=models.CharField(max_length=15)
   name=models.CharField(max_length=15)
   age=models.IntegerField()
   aadhar=models.IntegerField()
   documents=models.CharField(max_length=15)

class LoanAdmin(admin.ModelAdmin):
    list_display=('lid','loantype','name','age','aadhar','documents')
# Ex02 Django ORM Web Application

## Date: 29/09/2025

## AIM

To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1019" height="528" alt="image" src="https://github.com/user-attachments/assets/3d5dadfd-0fe0-4e0c-8fe4-1db9e6e37ab4" />

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

admin.py

```
from django.contrib import admin
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)
```

models.py

```
from django.db import models
from django.contrib import admin
class Movie(models.Model):
	Movie_name=models.CharField(max_length=50)
	Ratings=models.FloatField(primary_key="Ratings")
	Cast=models.CharField(max_length=50)
	Release_year=models.DateField()
	Genre=models.CharField(max_length=50)
class MovieAdmin(admin.ModelAdmin):
	list_display=('Movie_name','Ratings','Cast','Release_year','Genre')

class LoanAdmin(admin.ModelAdmin):
    list_display=('lid','loantype','name','age','aadhar','documents')
```
## OUTPUT

<img width="1026" height="700" alt="image" src="https://github.com/user-attachments/assets/fd819f85-e5d1-4379-8537-bfcaa66b7ad6" />

## RESULT
Thus the program for creating a database using ORM hass been executed successfully

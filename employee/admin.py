from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('employee_number', 'first_name','last_name','email','phone','sex')

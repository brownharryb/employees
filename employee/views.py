from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import EmployeeForm
from .models import Employee




def get_latest_employee_number():
	emp_numbers = list(Employee.objects.values_list('employee_number', flat=True))
	emp_numbers = [i.split('-') for i in emp_numbers]
	if not emp_numbers:
		return "EMP-0001"
	no = max([int(i[1] )for i in emp_numbers if len(i) > 1]) + 1
	return "EMP-{0:04d}".format(no)
		

class EmployeeView(View):
	template = 'employee_index.html'
	form_class = EmployeeForm


	def get(self, request, *args, **kwargs):
		form = self.form_class(initial={'employee_number':get_latest_employee_number()})
		return render(request, self.template, {'form':form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
		return render(request, self.template, {'form':form})



from django import forms
from .models import Employee


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('employee_number','first_name','middle_name','last_name','email',
					'phone','sex','date_of_birth')
		widgets = {
            'date_of_birth': DateInput(),
        }
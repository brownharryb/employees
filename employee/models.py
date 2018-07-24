from django.db import models
from .validators import (alpha_validator,phone_validator,
						employee_number_validator)


class Employee(models.Model):
	employee_number = models.CharField(max_length=12,unique=True, 
										validators=[employee_number_validator])
	first_name = models.CharField(max_length=250, validators=alpha_validator())
	middle_name = models.CharField(max_length=250,blank=True, null=True, validators=alpha_validator())
	last_name = models.CharField(max_length=250, validators=alpha_validator())
	email = models.EmailField(max_length=250, unique=True)
	phone = models.CharField(max_length=100, validators=phone_validator(), unique=True)
	sex = models.CharField(max_length=6,choices=(('Female', 'Female' ),('Male','Male')), default='Female')
	date_of_birth = models.DateField(verbose_name='Date Of Birth')


	def __str__(self):
		return self.employee_number
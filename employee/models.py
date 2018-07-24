from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def alpha_validator():
	'''Validate only alphabets and hyphens.'''
	return [validators.RegexValidator("^[a-zA-Z- ]*$",message="Invalid Input!")]

def phone_validator():
	'''Validate Phone Numbers.'''
	return [validators.RegexValidator("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$",
			message="Invalid Phone Number!")]

def employee_number_validator(emp_number):
	'''Validate Employee Number to 'EMP-XXXX'.'''
	if not re.match(r"^EMP-[0-9]{4,9}$",emp_number):
		raise ValidationError(_('Employee number should be "EMP-XXXX"!'))





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
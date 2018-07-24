
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



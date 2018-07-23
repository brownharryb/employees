from django.db import models
from django.core import validators


def alpha_validator():
	return [validators.RegexValidator("^[a-zA-Z- ]*$",message="Invalid Input!")]

def phone_validator():
	return [validators.RegexValidator("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$",
			message="Invalid Phone Number!")]


class Employee(models.Model):
	employee_number = models.CharField(max_length=100,unique=True)
	first_name = models.CharField(max_length=250, validators=alpha_validator())
	middle_name = models.CharField(max_length=250,blank=True, null=True, validators=alpha_validator())
	last_name = models.CharField(max_length=250, validators=alpha_validator())
	email = models.EmailField(max_length=250)
	phone = models.CharField(max_length=100, validators=phone_validator())
	sex = models.CharField(max_length=6,choices=(('Female', 'Female' ),('Male','Male')), default='Female')
	date_of_birth = models.DateField(verbose_name='Date Of Birth')
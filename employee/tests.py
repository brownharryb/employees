from django.test import TestCase
from .models import Employee
from .validators import employee_number_validator
from django.core.exceptions import ValidationError


class EmployeeTest(TestCase):

	def test_employee_number_validator(self):
		'''Employee number matches 'EMP-XXXX'.'''
		employee_number_validator("EMP-1234")
		employee_number_validator("EMP-12345")
		employee_number_validator("EMP-123456")
		for sample in ('sjkdbj','EMPo-kjbj','EMP-123','EMP-gfd12'):
			with self.assertRaises(ValidationError):
				employee_number_validator(sample)

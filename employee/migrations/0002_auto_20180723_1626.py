# Generated by Django 2.0.7 on 2018-07-23 16:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date Of Birth'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='Female', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', message='Invalid Input!')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', message='Invalid Input!')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=250, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z- ]*$', message='Invalid Input!')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='97697678687', max_length=100, validators=[django.core.validators.RegexValidator('^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$', message='Invalid Phone Number!')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='sex',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='Female', max_length=6),
        ),
    ]

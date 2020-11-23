from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee,candidatedb
from django import forms

class candidateform(forms.ModelForm):
    class Meta:
        model=candidatedb
        fields='__all__'





class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"



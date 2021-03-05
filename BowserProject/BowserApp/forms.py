from .models import Manager,Employee
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = ['first_name','last_name','address1','address1','zip_code','date_of_birth','company','email','username']
        widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}

# # class SignUpForm(UserEditForm):
#     class Meta(UserEditForm.Meta):
#         model = Manager
#         widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id','emp_email','emp_first_name','emp_last_name','emp_password','emp_address1','emp_address2','emp_zip_code','emp_city','emp_date_of_birth','emp_company','emp_mobile_no']
        

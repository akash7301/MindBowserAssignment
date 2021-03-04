from .models import Manager
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = ['first_name','last_name','address1','address1','zip_code','date_of_birth','company','email']
        widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}

# class SignUpForm(UserEditForm):
#     class Meta(UserEditForm.Meta):
#         model = Manager
#         widgets = {'date_of_birth': forms.DateInput(attrs={'type':'date'})}

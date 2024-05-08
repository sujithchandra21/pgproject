from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from django import forms
from .models import PG,Status_PG

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class RegisterPGOwner(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


# class PGForm(forms.Form):
#     pg_code = forms.CharField(max_length=20)
#     pg_name = forms.CharField(max_length=50)
#     address = forms.CharField(max_length=50)
#     rating = forms.FloatField()

class PGModelForm(forms.ModelForm):
    class Meta:
        model = PG
        fields = '__all__'

class StatusPgModelForm(forms.ModelForm):
    class Meta:
        model = Status_PG
        fields = '__all__'



# class RegistrationPgModelForm(forms.ModelForm):
#     class Meta:
#         model = Registration_PG
#         fields = '__all__'

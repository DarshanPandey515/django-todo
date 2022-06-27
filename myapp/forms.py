from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from myapp.models import todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title','Work_Status']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control focus:shadow-outline'}),
            'Work_Status': forms.RadioSelect(attrs={'class':'form-check'})
        }

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
    )

    class Meta:
        model = User 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class':'form-control form-control-lg'}),
            'first_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'last_name': forms.TextInput(attrs={'class':'form-control form-control-lg'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control form-control-lg'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control form-control-lg'}),
        }
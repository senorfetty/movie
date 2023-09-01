from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Account


class Register(UserCreationForm):
    username= forms.CharField(max_length=50,required=True, help_text='Required.')
    first_name= forms.CharField(max_length=100,required=True, help_text='Required.')
    last_name= forms.CharField(max_length=100, required=True, help_text='Required.')
    email= forms.EmailField(max_length=30, required=True, help_text='Required.')
    phone_number= PhoneNumberField()

    class Meta:
        model= Account
        fields = ( 'first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')

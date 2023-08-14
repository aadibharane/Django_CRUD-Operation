from django import forms
from .models import Account,Emp

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields=["id","name","email","address"]

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"
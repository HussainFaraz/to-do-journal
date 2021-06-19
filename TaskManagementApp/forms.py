import imp
from django import forms
from django.db import models
from django.db.models import fields
from .models import ToDoDB, User

class ToDoForm(forms.ModelForm):
    class Meta:
        model=ToDoDB
        fields = ['task']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email']
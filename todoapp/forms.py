from django import forms
from django.forms import ModelForm
from todoapp.models import *

class taskform(forms.ModelForm):

    class Meta:
        model = task
        fields = '__all__'
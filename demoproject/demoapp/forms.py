from django import forms
from django.forms.widgets import NumberInput
from .models import Logger

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)  
    email = forms.EmailField()
    reservationDate = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    # TextInput is the default input widget and does not need to be specified


class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
    
from django.db.models import fields
from traveloapp.models import destination
from django import forms

class updateform(forms.ModelForm):
    
    class Meta:
        model = destination
        fields= '__all__'
        # fields = ["name",'des','img','price','off']

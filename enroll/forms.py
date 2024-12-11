# from attr import fields
from cProfile import label
from django.core import validators
from django import forms
from .models import Bookambulance,Ambulance

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Bookambulance
       
        fields=['fname','lname','hname','address','uphone','age','gender']
        labels={'fname':'First Name','lname':'Last Name','hname':'Hospital Name','address':'Address','uphone':'Phone','age':'Age','gender':'Gender'}
        widgets={
            'fname':forms.TextInput(  attrs={'class':'form-control'}),
          'lname':forms.TextInput(attrs={'class':'form-control'}),
          'hname':forms.TextInput(attrs={'class':'form-control'}),
          'address':forms.TextInput(attrs={'class':'form-control'}),
          'uphone':forms.TextInput(attrs={'class':'form-control'}),
          # 'tambulance':forms.TextInput(attrs={'class':'form-control'}),
          'age':forms.TextInput(attrs={'class':'form-control'}),
        #   'gender':forms.TextInput(attrs={'class':'form-control'}),
 
        }
   
# class BasicForm(forms.ModelForm):
#       class Meta:
#         model = Basic

#         fields=['fac1','fac2','fac3','fac4']


class postForm(forms.ModelForm):
    class Meta:
        model= Ambulance
        fields = ['city', 'name','fac1','fac2','fac3','fac4']
        labels={ 'city':'type', 'name':'Facility','fac1':'Facility1','fac2':'Facility2','fac3':'Facility3','fac4':'Facility4'}
        widgets={'city':forms.TextInput (attrs={'class':'form-control'}),
        'name':forms.TextInput (attrs={'class':'form-control'}),
        'fac1':forms.TextInput (attrs={'class':'form-control'}),
        'fac2':forms.TextInput (attrs={'class':'form-control'}),
        'fac3':forms.TextInput (attrs={'class':'form-control'}),
        'fac4':forms.TextInput (attrs={'class':'form-control'}),}
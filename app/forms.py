
from django import forms
from django.core import validators

class StudentForms(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])

    boatch=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    
     #clean-element method allows boats catches
    def clean_element_boatch(self):
        b=self.cleaned_data['boatch']
        if len(b)>0:
            raise forms.ValidationError('bot')
    
    
    #clean method allows multiple vaues
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('email not match')
        
# class StudentForms(forms.Form):
#     name=forms.CharField(max_length=100)
#     age=forms.IntegerField()
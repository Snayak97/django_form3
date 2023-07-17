from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *


def SF(request):
    SFO=StudentForms()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudentForms(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('invalid')
    return render(request,'Sf.html',d)


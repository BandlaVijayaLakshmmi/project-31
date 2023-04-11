from django.shortcuts import render
# Create your views here.
from app.models import *
def department(request):
    EOM=Department.objects.all()
    d={'dep':EOM}
    return render(request,'Department.html',context=d)
def employee(request):
    EOe=Employee.objects.all()
    d={'emp':EOe}
    return render(request,'Employee.html',d)
    
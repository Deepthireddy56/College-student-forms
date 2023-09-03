from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_college(request):
    if request.method=='POST':
        #request.POST={'cn':SV,'sp':SV,'sl':SV}
        cn=request.POST['cn']
        p=request.POST['p']
        l=request.POST['l']

        CO=College.objects.get_or_create(CName=cn,Principal=p,Location=l)[0]
        CO.save()
        QLCO=College.objects.all()
        d={'QLCO':QLCO}
        return render(request,'display_college.html',d)
    
    return render(request,'insert_college.html')

def insert_student(request):
    if request.method=='POST':
        cn=request.POST['cn']
        sn=request.POST['sn']
        Sid=request.POST['Sid']

        CO=College.objects.get(CName=cn)
        STO=Student.objects.get_or_create(CName=CO,Sname=sn,Sid=Sid)[0]
        STO.save()
        QLSO=Student.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_student.html',d)
    return render(request,'insert_student.html')
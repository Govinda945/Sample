from django.shortcuts import render
from django.http import HttpResponse
from newapp.models import Contact

# Create your views here.
def home(request):
    return render (request,"index.html")

def index(request):
    if request.method=="POST":
        name= request.POST['Name']
        dob= request.POST['DOB']
        emailid= request.POST['Emailid']
        phone= request.POST['phone']
        gender= request.POST['gender']
        street=request.POST['street']
        flat=request.POST['flat']
        country= request.POST['country']
        imgfile=request.POST['filename']
        inst=Contact(name=name,dob=dob,email=emailid,phone=phone,gender=gender,street=street,flatno=flat,country=country,img=imgfile)
        inst.save()
        return HttpResponse("Thank You!")
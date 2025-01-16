from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todoapp.models import Todoo
# Create your views here.
def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        emailid=request.POST.get('email')
        pwd=request.POST.get('pwd')
        print(fnm,emailid,pwd)
        myuser=User.objects.create_user(fnm,emailid,pwd)
        myuser.save()
        return redirect('/login')
    return render(request,'sign.html')
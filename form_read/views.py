from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from .forms import FormContactForm
import pywhatkit
import datetime
import time

def showform(request):
    form= FormContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context= {'form': form }
    return render(request, 'contactform.html', context)

def reply(request):
    v1=request.POST.get('phone')
    v2=request.POST.get('msg')
    v3=request.POST.get('date')
    d=datetime.datetime.strptime(v3,'%Y-%m-%dT%H:%M')
    d=str(d)
    #print(d)
    #print(type(v1))
    v1='+'+v1
    #print(v1)
    x=True
    while x:
        #pywhatkit.playonyt("GeeksforGeeks")
        #print('hello world')
        time.sleep(1)
        t=datetime.datetime.now()
        c=t.strftime('%Y-%m-%dT%H:%M')
        y=datetime.datetime.strptime(c,'%Y-%m-%dT%H:%M')
        y=str(y)
        print(d)
        print(y)
        if y==d:
            print('hussain')
            #pywhatkit.sendwhatmsg("+919550650346","hi shoaib bhai this is automated message generated on specific time.",13,33,10,True,5)
            pywhatkit.sendwhatmsg_instantly(v1,v2,10,True,5)
            break
    
    return render(request,'reply.html',{'msg':v2})
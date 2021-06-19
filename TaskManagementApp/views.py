from collections import UserList
from django.contrib import messages
import imp
from django.forms import forms
from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.shortcuts import render,redirect
from .models import ToDoDB, User
from .forms import ToDoForm, UserForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# Create your views here.
def intro(request):

    if request.method == 'POST':
        User.objects.all().delete()
        ToDoDB.objects.all().delete()
        form = UserForm(request.POST or None)
        if(form.is_valid()):
            form.save()
            return render(request,'index.html')
        else:
           
            return render(request,'Home.html')
    else:
        return render(request,'Home.html')

def homeapp(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST or None)
        if(form.is_valid()):
            form.save()
            all_items = ToDoDB.objects.all()
            return render(request,'index.html',{'all_items' : all_items})
        else:
            all_items = ToDoDB.objects.all()
            return render(request,'index.html',{'all_items' : all_items})

    else:

        all_items = ToDoDB.objects.all()
        return render(request,'index.html',{'all_items' : all_items})
     
def delete(request,list_id):
    item = ToDoDB.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item Deleted..'))
    return redirect('homeapp')

def email(request):
    tasklist = []
    details=[]
    UserList = User.objects.values_list('name')
    name = UserList[0]
    emailList = User.objects.values_list('email')
    email = emailList[0]
    try:

        all_items = ToDoDB.objects.all().values_list()
        for i in range(0,5):
            tasklist.append(all_items[i][1])
        html_message = render_to_string('emaiL.html', {'all_items': tasklist , 'name':name})
        message = EmailMessage('Reminder - To-Do List', html_message, 'farazhussain651@gmail.com',email)
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()
        messages.success(request,('Email sent successfully!!'))
        ToDoDB.objects.all().delete()
        return render(request,'index.html')
        
    except:
        all_items = ToDoDB.objects.all().values_list()
        html_message = render_to_string('emaiL.html', {'all_items': tasklist , 'name':name})
        message = EmailMessage('Reminder - To-Do List', html_message, 'farazhussain651@gmail.com', email)
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()
        messages.success(request,('Email sent successfully!!'))
        ToDoDB.objects.all().delete()
        return render(request,'index.html')

def Logout(request):
    ToDoDB.objects.all().delete() 
  


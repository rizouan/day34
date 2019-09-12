from django.shortcuts import render, redirect
from .models import Employee
from django.core.paginator import Paginator
from lesson4app.forms import EmployeeForm, ContactForm
from django.contrib import messages
from django.core.mail import BadHeaderError, EmailMessage


# Create your views here.

def index(request):
    emp = Employee.objects.all()


    #employees = Employee.objects.all()
    context = {'title': 'Welcome', 'employees': emp}
    return render(request,"index.html",context)

def create(request):
    if request.method == "POST":
        form= EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert Successfull')
                return redirect('/index')
                # return redirect('/')
            except:
                pass
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})

def edit(request, id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,request.FILES)
    return render(request,'edit.html', {'employee':employee,'form':form})

def update(request, id):
    employee=Employee.objects.get(id=id)
    form= EmployeeForm(request.POST,request.FILES,instance=employee)
    if form.is_valid():
        try:
            form.save()
            messages.error(request,'Update Successfull')
            return redirect('/index')
            # return redirect('/')
        except:
            pass
    else:
        messages.error(request,form.error)
    return render(request,'edit.html', {'employee':employee,'form':form})

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/index")


def test(request):
    if request.method == "POST":
        form= EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.error(request,'Insert Successfull')
                return redirect('/index')
                # return redirect('/')
            except:
                pass
        else:
            pass
    else:
        form = EmployeeForm()
    return render(request,'test.html',{'form':form})


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():

            subject        = form.cleaned_data['subject']
            form_email     = form.cleaned_data['to']
            message        = form.cleaned_data['message']

            recipient_list = []
            recipient_list.append(form_email)
            try:
                emailobj = EmailMessage(subject, message, to = recipient_list)
                emailobj.send()
            except BadHeaderError:
                return Httpresponse('Invalid header Found')
            return redirect('/index')
    return render(request, "email.html",{'form': form})

from django.shortcuts import redirect, render
from .models import Todo, contact
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context={
        "page":"Home context",
        "logged":True 
    }
    return render(request,'home.html',context)

def Contact(request):
    contact_obj = contact.objects.all()
    print(contact_obj)
    context={
        "page":"contact context",
        "logged":False,
        "contacts":contact_obj}
    return render(request,'contact.html',context)

def about(request):
    context={
        "page":"about context",
        "logged":False
    }
    return render(request,'about.html',context)

@login_required(login_url="/")
def todo(request):
    if request.method =="POST":
        todo =request.POST['todo']
        if todo is not None:
            todo_obj=Todo(todo_name=todo,user=request.user)
            todo_obj.save()
        return redirect('/todo')
    todo_object=Todo.objects.filter(user=request.user)
    context={
        "todo_obb":todo_object
    }
    return render(request,'todo.html',context)

def delete_as_complete(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.delete()
    except Todo.DoesNotExist:
        pass
    return redirect("/todo")
def mark_as_complete(request,id):
    try:
        todo=Todo.objects.get(id=id)
        todo.is_complete =True
        todo.save()
    except Todo.DoesNotExist:
        pass
    return redirect("/todo")

def register(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user=User(email=email,username=email)
        user.set_password(password)
        user.save()
        
    return render(request,"register.html")

def login_page(request):
    if request.method=="POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user=User.objects.filter(email=email).first()
        if user is None:
            messages.success(request,"User not found")
            return redirect("/login_page")
        print(user.email)
        print(password)
        user_auth=authenticate(username=email,password=password)
        if user_auth:
            login(request,user)
            return redirect("/todo")
        else:
            messages.success(request,"you entered wrong password!")
            return redirect("/login_page")
    return  render(request,'login.html')
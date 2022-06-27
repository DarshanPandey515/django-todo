from django.shortcuts import redirect, render
from .models import todo
from django.contrib import messages, auth
from .forms import TodoForm,UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        data = todo.objects.filter(user = user).order_by('-Work_Status')
        return render(request, 'index.html',{'data':data})
    else:
        return render(request, 'index.html')

@login_required(login_url='/')
def add(request):
    if request.user.is_authenticated:
        user = request.user
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('index')
        else:
            form = TodoForm()
    else:
        form = TodoForm()
    return render(request, 'add.html', {'form':form})

# if request.user.is_authenticated:
#         user = request.user
#         print(user)
#         form = TODOForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             todo = form.save(commit=False)
#             todo.user = user
#             todo.save()
#             print(todo)
#             return redirect("home")
@login_required(login_url='/')
def removelist(request, id):
    data = todo.objects.filter(pk=id)
    data.delete()
    return redirect('index')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    auth.logout(request)
    return render(request, 'index.html')
    

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'signup.html',context)


def edit(request, id):
    if request.method == 'POST':
        data = todo.objects.filter(pk=id).first()
        form = TodoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        data = todo.objects.filter(pk=id).first()
        form = TodoForm(instance=data)
    context={
        'form':form
    }
    return render(request, 'edit.html',context)
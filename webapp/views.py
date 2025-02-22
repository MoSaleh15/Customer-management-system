from django.shortcuts import render , redirect , get_object_or_404
from .forms import CreateUserForm , LoginForm , CreateRecoardForm , UbdateRecoardForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Record
from django.db.models import Q
import logging
from django.contrib import  messages

def index(request):
    return render(request,'web/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registeration is Successfuly')
            return redirect('login')
    else:
        form = CreateUserForm()
     
    context = {
        'form':form
    }

    return render(request,'web/register.html',context)



def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request , data =request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request , username=username , password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Login is Successfuly')
                return redirect('dashboard')
    else:
        form = LoginForm()        

    context = {
        'form':form
    }

    return render(request,'web/login.html',context)    

@login_required(login_url='login')
def dashboard(request):
    record = Record.objects.all()
    return render(request,'web/dashboard.html',context={'record':record})

def my_logout(request):
    logout(request)
    messages.success(request,'Logout is Successfuly')
    return redirect('login')



@login_required(login_url='login')
def create_record(request):
    form = CreateRecoardForm()
    if request.method == 'POST':
        form = CreateRecoardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Create Recoard is Successfuly')
            return redirect('dashboard')    
    else:
        form = CreateRecoardForm()

    context = {
        'form':form
    }

    return render(request,'web/record.html',context)    


@login_required(login_url='login')
def record_view(request,record_id):
    all_recoard = get_object_or_404(Record,id = record_id)
    context = {
        'record':all_recoard
    }
    return render(request,'web/view.html',context)

@login_required(login_url='login')
def ubdate_record(request,record_id):
    record = get_object_or_404(Record,id =record_id)
    form = UbdateRecoardForm(instance=record)#instance => دي هترجعلي الفورم فيها الداتا ال في الريكورد 
    if request.method == 'POST':
        form = UbdateRecoardForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,'Ubdate Recoard is Successfuly')
            return redirect('dashboard')
    context = {
        'form':form
    }

    return render(request,'web/ubdate.html',context)     

@login_required(login_url='login')
def delete_record(request,record_id):
    record = get_object_or_404(Record,id =record_id)
    record.delete()
    messages.success(request,'Delete Recoard is Successfuly')
    return redirect('dashboard')

logger = logging.getLogger(__name__)
@login_required(login_url='login')
def search(request):
    qeury = request.GET.get('qeury')#اي حاجه هبحث عنه
    reslut = []# هيتسجل فيه ال حاجه ال هبحث عنها 
    try:
        if qeury :
            reslut = Record.objects.filter(Q(first_name__icontains=qeury) | Q(id__icontains=qeury))#هياخد ال هبحث عنه ويروح يقارنه بال داتا بيز 
    except Exception as e:
        logger.error("Error during search: %s",e)

    return render(request,'web/search.html',context={'result':reslut , 'qeury':qeury})

def custom_not_found(request,exception):
    return render(request,'web/404.html',status=404)
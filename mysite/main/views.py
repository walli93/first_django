from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .models import Tutorials,Vehicles,Essays
from django.contrib import messages

# Create your views here.
'''def homepage(request):
    return HttpResponse("Wow! this is a <strong>awesome</strong> web page.")'''

def homepage(request):
    return render(request = request,
    template_name='main/home.html',
    context = {"tutorials":Tutorials.objects.all,"vehicles":Vehicles.objects.all,"essays":Essays.objects.all})

def add_user(request):
    return render(request = request,
    template_name='main/add_user.html')


def add_vehicle(request):
    if request.method == 'POST':
        if request.POST.get('vehicle_name') and request.POST.get('reg_no') and request.POST.get('yom'):
            post=Post()
            post.vehicle_name = request.POST.get('vehicle_name')
            post.reg_no = request.POST.get('reg_no')
            post.yom = request.POST.get('yom')
            post.save

            return render(request,'main/add_user.html')

        else:
            return render(request,'main/add_user.html')

'''def logout(request):
    return render(request = request,
    template_name='main/home.html')'''


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {{username}}")
            login(request, user)
            messages.success(request, f"New account created: {{username}}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{{msg}}: {{form.error_messages[msg]}}")
        
    form = UserCreationForm
    return render(request,
    template_name="main/register.html",
    context={"form":form})



from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *


def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = CustomUser.objects.get(email =email).username
            user = authenticate(request, username=username,password=password) 
        
            if user is not None:

                login(request,user)
               
                return redirect('index')
            else:
                return render(request,'login.html',{'form':form})

    form = LoginForm()
    context = {
        'form':form
    }
    return render(request,'login.html',context)



def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})
    form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def user_logout(request):
    logout(request)
    return redirect('index')


def profil(request):
    if request.method == 'POST':
        profilId = request.POST['sil']
        profil = Profil.objects.get(id = profilId)
        profil.delete()
        # !
    else:
        return render(request,'profil.html')
    return render(request,'profil.html')


def profilManage(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.owner = request.user
            profil.save()
            return redirect('profil')
            
    form = ProfilForm()
    return render(request,'profilManage.html',{'form':form})



    
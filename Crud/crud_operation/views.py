from django.shortcuts import render,HttpResponseRedirect
from .models import user
from .forms import adding_data

def registration(request):
    stud=user.objects.all()
    if request.method=='POST':
        fm=adding_data(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=pw)
            reg.save()
            fm=adding_data()    
    else:
        fm=adding_data()
    return render(request,'addshow.html',{"form":fm,'stu':stud})

def delete(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        fm=adding_data(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi=user.objects.get(pk=id)
        fm=adding_data(instance=pi)
    return render(request,'update.html',{"form":fm})
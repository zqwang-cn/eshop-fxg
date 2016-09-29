#encoding:utf-8
from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from forms import SignupForm,SigninForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if request.user.is_authenticated():
        return redirect(reverse('shop.index'))
    if request.method=='POST':
        form=SigninForm(request.POST)
        if not form.is_valid():
            return render(request,'signin.html',{'form':form})
        phone_number=form.cleaned_data['phone_number']
        password=form.cleaned_data['password']
        user=authenticate(username=phone_number,password=password)
        if user is None:
            return render(request,'signin.html',{'form':form})
        login(request,user)
        next=form.cleaned_data['next']
        if not next:
            return redirect(reverse('shop.index'))
        return redirect(next)
    else:
        next=request.GET.get('next')
        form=SigninForm(initial={'next':next})
        return render(request,'signin.html',{'form':form})

def signup(request):
    if request.user.is_authenticated():
        return redirect(reverse('shop.index'))
    if request.method=='POST':
        form=SignupForm(request.POST)
        if not form.is_valid():
            return render(request,'signup.html',{'form':form})
        phone_number=form.cleaned_data['phone_number']
        password=form.cleaned_data['password']
        user=User.objects.create_user(username=phone_number,password=password)
        user.save()
        print 'yes'
        #user=authenticate(username=email,password=password)
        #if user is not None:
        #    login(request,user)
        return redirect(reverse('shop.index'))
    else:
        form=SignupForm()
        return render(request,'signup.html',{'form':form})

def signout(request):
    logout(request)
    return redirect(reverse('account.signin'))

@login_required
def detail(request):
    user=request.user
    return render(request,'account_detail.html',{'user':user})

def sendcode(request):
    pass

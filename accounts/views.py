from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import CustomUserCreationForm

# Create your views here.

def signup_view(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form=CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form=CustomUserCreationForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')
def login_view(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                username_or_email=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
            username_or_email=request.POST.get('username')
            password=request.POST.get('password')
            try:
                user_obj = User.objects.get(Q(username=username_or_email) | Q(email=username_or_email))
                username = user_obj.username  # دریافت یوزرنیم معادل ایمیل
            except User.DoesNotExist:
                username = username_or_email
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required #users can only access this view if they are logged in
def logout_view(request):
    logout(request)
    return redirect('/')
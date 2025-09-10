from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import LoginForm, RegisterForm, CheckOtpForm
from .models import Otp, User
import ghasedakpack
from random import randint
from django.utils.crypto import get_random_string
from uuid import uuid4

SMS = ghasedakpack.Ghasedak("7edce8bc3120a269e9fa4b24c50e2caf8b820cd54ab1efe69b6b896da175c14b")

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        
        return render(request, "account/login.html", {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error("phone", "invalid user data")
        
        else:
            form.add_error("phone", "invalid data")
            
        return render(request, "account/login.html", {'form': form})
    
    
class OtpLoginView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "account/otp_login.html", {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification({'receptor': cd["phone"], 'type': '1', 'template': 'randcore', 'param1': randcode, 'param2': 'hi'})
            token = str(uuid4)
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error("phone", "invalid data")
            
        return render(request, "account/otp_login.html", {'form': form})
    

class CheckOtpView(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, "account/check_otp.html", {'form': form})
    
    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect('/')
        else:
            form.add_error("phone", "invalid data")
            
        return render(request, "account/check_otp.html", {'form': form})
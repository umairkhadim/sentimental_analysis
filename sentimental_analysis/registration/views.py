from datetime import date

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import *
from django.contrib.auth import authenticate, login, logout
# from sentimental_analysis.home import urls

from django.contrib import messages
# from .models import *
# from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator
# from .decorators import login_register_check
# from django.core.mail import EmailMessage
# # Function for customer signup
# from .tokens import account_activation_token


# @login_register_check
def customer_signup(request):
    signup_form = SignUpForm()
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.save()
            return redirect('login')

    context = {
        'form': signup_form
    }
    return render(request, 'registration/signup.html', context)


# Function for customer login

# @login_register_check
def customer_login(request):
    login_form = LoginForm()
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "incorrect Username or Password")

    context = {
        'form': login_form
    }
    return render(request, 'registration/login.html', context)


# Function for customer logout

# @login_required(login_url='login')
def customer_logout(request):
    logout(request)
    return redirect('login')


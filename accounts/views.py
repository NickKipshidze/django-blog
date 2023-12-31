from django.shortcuts import render, redirect
from django.contrib import auth
from django.views import View
from . import forms

# Create your views here.

class LoginView(View):
    def get(self, request):
        form = forms.LogInForm()
        return render(request, "login.html", {"form": form})
    
    def post(self, request):
        form = forms.LogInForm(request, data=request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username = form.cleaned_data.get("username"), 
                password = form.cleaned_data.get("password")
            )
            if user is not None:
                auth.login(request, user)
                return redirect(f"/{user}")
        
        return render(request, "login.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("home")

class SignupView(View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, "signup.html", {"form": form})
    
    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
        return render(request, "signup.html", {"form": form})
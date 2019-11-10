from django.shortcuts import render, redirect
from django.contrib import auth
from homepage.forms import UserLoginForm

# Create your views here.
def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')

def login(request):
    """Return a login page"""
    if request.method=="POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                                    
            
            if user:
                auth.login(user=user, request=request)
                return redirect("user_homepage")
            
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})

def registration(request):
    """Render the registration page"""
    return render(request, 'registration.html')
    
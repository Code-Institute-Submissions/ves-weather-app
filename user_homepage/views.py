from django.shortcuts import render

# Create your views here.
def user_homepage(request):
    return render(request, 'userhomepage.html')
    
def index(request):
    return render(request, 'base.html')
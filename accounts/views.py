from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def index(request):
    ''' Renders "index.html" '''
    return render(request, "index.html")

def logout(request):
    ''' logout functionality '''
    auth.logout(request)
    messages.success(request, 'you have been logged out')
    return redirect(reverse('index'))
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import LoginForm

# Create your views here.
def index(request):
    ''' Renders "index.html" '''
    return render(request, "index.html")

def logout(request):
    ''' logout functionality '''
    auth.logout(request)
    messages.success(request, 'you have logged out')
    return redirect(reverse('index'))

def login(request):
    ''' Renders "login.html" '''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'you have logged in')
            else:
                login_form.add_error(None, 'an error occured')

    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})
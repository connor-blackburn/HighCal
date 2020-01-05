from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, UserRegistrationForm
from portfolio.models import Portfolio
from products.models import Product
from posts.models import Post

# Create your views here.
def index(request):
    ''' Renders "index.html" '''
    portfolios = Portfolio.objects.all()
    products = Product.objects.all()
    posts = Post.objects.all()
    return render(request, "index.html", {"portfolios": portfolios, "products": products, "posts": posts})

def user_profile(request):
    ''' renders users profile page '''
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})

@login_required
def logout(request):
    ''' logout functionality '''
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def login(request):
    ''' Renders "login.html, allows user to log in" '''
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully logged in')
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'An error occured')

    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def registration(request):
    ''' registration page ''' 
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have successfully registered')
            else:
                messages.error(request, 'An error occured')
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        'registration_form': registration_form})
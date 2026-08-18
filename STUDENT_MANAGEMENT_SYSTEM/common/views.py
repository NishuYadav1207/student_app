from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'common/home.html')


def about(request):
    return render(request, 'common/about.html')


def faq(request):
    return render(request, 'common/faq.html')


def contactus(request):
    return render(request, 'common/contactus.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(request, 'common/login.html')


def logout_view(request):

    logout(request)

    return redirect('home')
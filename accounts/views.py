from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            context = {
                'msg': 'Invalid user!',
                'title': 'Login Error'
            }
    else:
        context = {
            'msg': None,
            'title': 'Pls login!',
            'next': request.GET.get('next')
        }

    if request.user.is_authenticated:
        if next:
            return HttpResponseRedirect(next) 
        else:
            return HttpResponseRedirect(reverse('polls:index'))

    return render(request, 'accounts/account_login.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))

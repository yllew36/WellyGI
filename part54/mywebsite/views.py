from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login, logout


class IndexView(TemplateView):
    template_name = 'index.html'


def index(request):
    context = {
        'page_title': 'Home',
    }

    return render(request, 'index.html', context)


def loginView(request):
    context = {
        'page_title': 'Login',
    }

    if request.method == "POST":
        # print(request.POST)

        username_login = request.POST['username']
        password_login = request.POST['password']

        # print(username)
        # print(password)

        user = authenticate(request, username=username_login,
                            password=password_login)
        # print(user)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    # username_ucup = 'ucup'
    # password_ucup = 'rahasia123'

    # user = authenticate(request, username = username_ucup, password=password_ucup)
    # print (user)

    # login (request,user)

    return render(request, 'login.html', context)

def logoutView(request):
    context = {
        'page_title': 'Logout',
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            # print("proses logout")

            logout(request)

        return redirect('index')



    return render(request, 'logout.html', context)

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Oferta
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def get_all_offerts(request):
    offers = Oferta.objects.all()
    context = {'oferty': offers}
    return render(request, 'MotoSell/oferty.html', context)


def login_template(request):
    return render(request, 'registration/login.html')


def login(request):
    user = User.objects.create_user(request.name)
    return render(request, 'registration/login.html')


def register_template(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            messages.success(request, 'Form submission successful')
            f.save()
            return render(request, 'registration/register.html', {'form': f})
    else:
        f = UserCreationForm()
    return render(request, 'registration/register.html', {'form': f})


def logout_view(request):
    logout(request)
    return render(get_all_offerts)

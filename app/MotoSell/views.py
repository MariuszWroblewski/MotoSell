from django.shortcuts import render
from .models import Oferta
from django.contrib.auth import logout

# Create your views here.


def get_all_offerts(request):
    offers = Oferta.objects.all()
    context = {'oferty': offers}
    return render(request, 'MotoSell/oferty.html', context)


def login_template(request):
    return render(request, 'registration/login.html')


def register_template(request):
    return render(request, 'registration/register.html')


def logout_view(request):
    logout(request)
    return render(get_all_offerts)

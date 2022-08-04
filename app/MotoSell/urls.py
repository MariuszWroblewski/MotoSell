from django.urls import path, include
from . import views
from django.contrib.auth import urls


urlpatterns = [
    path('', views.get_all_offerts, name='home'),
    path('register', views.register_template, name='register'),
    path('login', views.login_template, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('accounts/', include(urls)),
]

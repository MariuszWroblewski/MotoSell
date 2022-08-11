from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUser, LogoutUser

app_name = 'user'

urlpatterns = [
    path('register/', CreateUser.as_view(), name=CreateUser.name),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutUser.as_view(), name=LogoutUser.name),
]

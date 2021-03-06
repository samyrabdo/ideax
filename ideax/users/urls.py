from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile, SignUpView

urlpatterns = [
    path('accounts/login/', auth_views.login, name='login'),
    path('accounts/logout/', auth_views.logout, name='logout'),
    path('accounts/sign-up/', SignUpView.as_view(), name='sign-up'),
    path('users/profile/', profile, name='profile'),
]

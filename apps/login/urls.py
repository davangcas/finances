from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.login.views.login import LoginFormView, ChangePasswordView

app_name = "login"

urlpatterns = [
    path('', LoginFormView.as_view(), name="login"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('logout/', LogoutView.as_view(next_page='login:login'), name="logout"),
]
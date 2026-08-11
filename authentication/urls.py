from django.urls import path
from .views import *


urlpatterns = [
  path('sign-up/', SignUpView, name="sign-up"),
  path('login/', LoginView, name="accounts-login"),
  path('logout/', LogoutView, name="accounts-logout"),
  path('account/', AccountView, name="accounts-account"),
  path('password/change/', ChangePasswordView, name="accounts-password"),

]
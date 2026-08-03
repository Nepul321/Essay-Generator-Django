from django.shortcuts import render, HttpResponseRedirect, redirect
from .decorators import unauthenticated_user
from django.contrib.auth import login,logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *

@unauthenticated_user
def LoginView(request, *args, **kwargs):
  template = "login.html"
  next = ""
  if request.GET:
    next = request.GET['next']
  form = LoginForm(request, data=request.POST or None)
  if form.is_valid():
    user = form.get_user()
    login(request, user)
    if next == "":
      return HttpResponseRedirect('/')
    else:
      return HttpResponseRedirect(next)
    
  context = {'form' : form}
  return render(request, template, context)

@login_required
def LogoutView(request, *args, **kwargs):
   logout(request)
   return redirect('accounts-login')


@login_required
def AccountView(request, *args, **kwargs):
   template = "account.html"
   form = AccountUpdateForm(instance=request.user)
   if request.method == "POST":
     form = AccountUpdateForm(request.POST, instance=request.user)
     if form.is_valid():
         form.save()
         return redirect('account-view')
   context = {
      'form' : form
   }

   return render(request, template, context)


@login_required
def ChangePasswordView(request, *args, **kwargs):
  template = "change_password.html"
  if request.method == "POST":
      form = ChangePasswordForm(request.user, request.POST)

      if form.is_valid():
          user = form.save()

            # Prevent user from being logged out
          update_session_auth_hash(request, user)

          return redirect("accounts-account")
  else:
      form = ChangePasswordForm(request.user)
  context = {
      'form' : form,
  }

  return render(request, template, context)
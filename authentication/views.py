from django.shortcuts import render, HttpResponseRedirect, redirect
from .decorators import unauthenticated_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import *

@unauthenticated_user
def LoginView(request, *args, **kwargs):
  template = "login.html"
  next = ""
  if request.GET:
    next = request.GET['next']
  form = AuthenticationForm(request, data=request.POST or None)
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
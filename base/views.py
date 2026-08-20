from django.shortcuts import render, redirect
from .forms import EssayForm, EssayEditForm
from .service import ask_gemini
from django.contrib.auth.decorators import login_required
from .models import Essay

@login_required
def HomeView(request, *args, **kwargs):
	template = "home.html"
	form = EssayForm()
	if request.method == "POST":
		prompt = request.POST.get("title")
		paragraphs = request.POST.get("paragraphs")
		level = request.POST.get("grade_level")
		reply = ask_gemini(prompt, paragraphs, level)
		form = EssayForm(request.POST)
		if form.is_valid():
			form.instance.content = reply
			form.instance.user = request.user
			form.save()
			return redirect('essays')
	context = {
      'form' : form
	}

	return render(request, template, context)


@login_required
def EssayListView(request, *args, **kwargs):
	template = "items.html"
	qs = Essay.objects.all().filter(user=request.user)
	context = {
       'qs' : qs
	}
	return render(request, template,context)

@login_required
def EssayView(request, key, *args, **kwargs):
	template = "detail.html"
	qs = Essay.objects.all().filter(key=key)
	if not qs:
		return redirect('essays')
	obj = qs.first()
	if obj.user != request.user:
		return redirect('essays')
	form = EssayEditForm(instance=obj)
	if request.method == "POST":
		form = EssayEditForm(request.POST, instance=obj)
		form.save()
	context = {
        'obj' : obj,
        'form' : form,
	}
	return render(request, template, context)

@login_required
def EssayDeleteView(request, key, *args, **kwargs):
	template = "delete.html"
	qs = Essay.objects.all().filter(key=key)
	if not qs:
		return redirect('essays')
	obj = qs.first()
	if obj.user != request.user:
		return redirect('essays')
	if request.method == "POST":
		obj.delete()
		return redirect('essays')
	context = {
        'obj' : obj
	}
	return render(request, template, context)
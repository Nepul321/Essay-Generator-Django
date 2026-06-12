from django.shortcuts import render, redirect
from .forms import EssayForm
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
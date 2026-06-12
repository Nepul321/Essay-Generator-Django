from django.shortcuts import render, redirect
from .forms import EssayForm
from .service import ask_gemini


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
			form.instance.content = reply['markdown']
			form.instance.user = request.user
			form.save()
			return redirect('/')
	context = {
      'form' : form
	}

	return render(request, template, context)
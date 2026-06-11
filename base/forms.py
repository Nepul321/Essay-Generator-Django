from django import forms
from .models import *

class EssayForm(forms.ModelForm):
	class Meta:
		model = Essay
		fields = ('title', 'paragraphs', 'grade_level', 'content')

		widgets = {
           'title' : forms.TextInput(attrs={'class' : 'form-control'}),
           'paragraphs' : forms.NumberInput(attrs={'class' : 'form-control'}),
           'grade_level' : forms.TextInput(attrs={'class' : 'form-control'}),
           'content' : forms.Textarea(attrs={'class' : 'form-control'})
		}
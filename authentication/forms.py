from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

		widgets = {
			'username' : forms.TextInput(attrs={'class' : 'form-control'}),
			'first_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'last_name' : forms.TextInput(attrs={'class' : 'form-control'}),
			'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
		}

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        ),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )
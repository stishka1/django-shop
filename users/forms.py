from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SignupForm(forms.ModelForm):
	username = forms.CharField(max_length=200, label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(label='Почтовый ящик', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] != cd['password2']:
			raise forms.ValidationError('Пароли не совпадают!')
		return cd['password2']
	# def __init__(self, *args, **kwargs):
	# 	super(SignupForm, self).__init__(*args, **kwargs)
	# 	self.fields['password1'].widget.attrs['class'] = 'form-control'
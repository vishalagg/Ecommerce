from django import forms
from django.contrib.auth import get_user_model

class ContactForm(forms.Form):
	Fullname = forms.CharField(
		widget = forms.TextInput(
				attrs = {
					"class":"form-control",
					"placeholder":"<Enter your name>"
					}
			)
		)
	Email = forms.EmailField(
		widget = forms.EmailInput(
				attrs = {
					"class":"form-control",
					"placeholder":"<Enter your email>"
					}
			)
		)
	Content = forms.CharField(
		widget = forms.Textarea(
				attrs = {
					"class":"form-control",
					"placeholder":"Write Something!!!!"
					}
			)
		)

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if not "@" in email:
	#		raise forms.ValidationError("Wrong Email")
	#	return email

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

User = get_user_model()
class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)

	#To handle duplicate username
	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is already taken. TRY another!!")
		return username

	#To handle duplicate email
	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("This Email is already regitered.")
		return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Password Didnt match")
		return data
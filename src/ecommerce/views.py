from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from products.models import Product
from cart.get_cart import get_cart

from .forms  import ContactForm,LoginForm,RegisterForm

def home_page(request):
	context = {}
	try:
		cart_obj = get_cart(request)
		context['total_products'] = cart_obj.products.count()
	except:
		pass
	return render(request,'index.html',context)

# def about_page(request):
# 	return render(request,'index.html',{})

def contact_page(request):
	contact_form = ContactForm()
	try:
		cart_obj = get_cart(request)
		total_products = cart_obj.products.count()
	except:
		total_products=0
	context = {
		'form' : contact_form,
		'title' : "Contact",
		'total_products':total_products,
	}
	return render(request,'contact/view.html',context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		'form':form
	}
	#print(request.user.is_authenticated())
	if form.is_valid():
		#print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request,username=username,password=password)
		#print(request.user.is_authenticated())
		if user is not None:
			print("Now You:")
			login(request,user)
			print(request.user.is_authenticated())
			return redirect("/login")
		else:
			print("Error")
	return render(request,"auth/login.html",{'form':form})

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		'form' : form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		newUser = User.objects.create_user(username,email,password)
	return render(request,"auth/register.html",context)


class SearchProduct(ListView):
	template_name = 'search.html'

	def get_queryset(self,*args,**kwargs):
		q = self.request.GET.get('q')
		if q is not None:
			return Product.objects.all().filter(title__icontains=q)
		return Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(SearchProduct, self).get_context_data(*args, **kwargs)
		try:
			cart_obj = get_cart(self.request)
			context['total_products'] = cart_obj.products.count()
		except:
			pass
		return context

def logout_view(request):
    logout(request)
    return redirect("home")
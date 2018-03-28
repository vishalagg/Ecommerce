from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import Product

from cart.get_cart import get_cart
from django.urls import reverse
# Create your views here.



@login_required(login_url="/login")
def cart_total(request,cart_obj):
	#cart_obj = get_cart(request)
	products = cart_obj.products.all()
	total = 0
	for e in products:
		total = total+e.price
	print("ye hai",total)
	cart_obj.total = total
	cart_obj.save()
	return total

@login_required(login_url="/login")
def cart_home(request):	
	cart_obj = get_cart(request)
	total = cart_total(request,cart_obj)
	total_products = cart_obj.products.count()
	discount = total_products*200
	context = {
		"cart": cart_obj,
		"total": total,
		"discount": discount,
		"total_products":total_products,
	}
	#print("SEE HERE:")
	#print(cart_obj.products.all())

	return render(request,"cart/home.html",context)


@login_required(login_url="/login")
def cart_update(request):
	product_id = request.POST.get('product_id')
	reToCart = request.POST.get('reToCart')
	#print("Helolo")
	print("productID:",product_id)
	product_obj = Product.objects.get(id=product_id)
	print(product_obj)
	cart_obj = get_cart(request)
	print("CART_OBJ:",cart_obj)
	if product_obj in cart_obj.products.all():
		cart_obj.products.remove(product_obj)
	else:
		cart_obj.products.add(product_obj)
	cart_total(request,cart_obj)
	total_products = cart_obj.products.count()
	if reToCart=="True":
		return redirect("cart")
	return redirect(reverse('detail',kwargs={'pk':product_id}))
from django.shortcuts import render, get_object_or_404 #=>use in function based detailview
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Product
from cart.models import Cart
from cart.get_cart import get_cart

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/list.html'   #=>default is product_list.html
	#default context is qs here
	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		try:
			cart_obj = get_cart(self.request)
			# user = self.request.user
			# if user:
			# 	qs = Cart.objects.filter(user=user)
			# 	if qs.count() == 1:
			# 		cart_obj = qs.first()
			# 	else:
			# 		cart_obj = None
			context['total_products'] = cart_obj.products.count()
			context['cart'] = cart_obj
		except:
			pass
		return context

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		try:
			cart_obj = get_cart(self.request)
			# user = self.request.user
			# if user:
			# 	qs = Cart.objects.filter(user=user)
			# 	if qs.count() == 1:
			# 		cart_obj = qs.first()
			# 	else:
			# 		cart_obj = None
			context['total_products'] = cart_obj.products.count()
			context['cart'] = cart_obj
		except:
			pass
		return context


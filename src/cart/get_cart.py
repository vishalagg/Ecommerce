from .models import Cart

def get_cart(request):
	user = request.user
	qs = Cart.objects.filter(user=user)
	#print(qs.count())
	if qs.count() == 1:
		#print("Already hai")
		cart_obj = qs.first()
	else:
		cart_obj = Cart.objects.create(user=user)
		#print("I am here")
	return cart_obj
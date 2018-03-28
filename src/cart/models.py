from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL
# Create your models here.
class Cart(models.Model):
	user 	 =	models.ForeignKey(User, blank=True, null=True)
	products =  models.ManyToManyField(Product, blank=True)
	total 	 = 	models.DecimalField(max_digits=20,default=0.00,decimal_places=2)

	def __str__(self):
		return str(self.user)
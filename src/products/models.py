from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=20.50)
	image = models.ImageField(upload_to='products/' , null =True, blank=True)

	def get_absolute_url(self):
		return reverse('detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.title
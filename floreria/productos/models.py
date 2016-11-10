from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Product (models.Model):

	name=models.CharField(max_length=100)
	desc=models.TextField()
	price=models.IntegerField()
	image=models.ImageField(upload_to="flowers")
	available=models.BooleanField(default=True)
	slug=models.SlugField(max_length=200)

	def get_absolute_url(self):
		return reverse('products:detail', args=[self.slug])

	def __str__(self):
		return self.name
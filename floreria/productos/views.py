from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product
from cart.forms import CartAddProductForm
# Create your views here.

class ListView(View):
	def get(self, request):
		products=Product.objects.all()
		
		template_name='products/catalog.html'

		context={
		'products':products
		}

		return render(request, template_name, context)

class DetailView(View):
	def get (self, request, slug):
		product=get_object_or_404(Product, slug=slug)

		template_name='products/detail.html'
		form = CartAddProductForm()

		context={
		'product':product,
		'form':form
		}

		return render(request, template_name, context)
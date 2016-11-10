from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import CartAddProductForm
from django.core.urlresolvers import reverse
from django.views.generic import View
from .cart import Cart
from productos.models import Product
# Create your views here.

class AddProduct(View):
	def post(self, request, product_id):
		cart = Cart(request)
		product = get_object_or_404(Product, id=product_id)
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(
				product=product,
				quantity=cd['quantity'],
				update_quantity=cd['update'])
			return redirect('cart:cart_detail')

class Remove(View):
	def get(self, request, product_id):
		cart = Cart(request)
		product = get_object_or_404(Product, id=product_id)
		cart.remove(product)
		return redirect('cart:cart_detail')

class CartDetail(View):
	def get(self, request):
		cart=Cart(request)
		form=CartAddProductForm()
		
		template_name='cart/detail.html'
		context={
		'cart':cart,
		'form':form
		}
		return render(request, template_name, context)

#class Prueba(View):
#	def get(self, request, product_id):
#		cart = Cart(request)
#		product = get_object_or_404(Product, id=product_id)
#		form = CartAddProductForm(request.GET)
#		if form.is_valid():
#			cd = form.cleaned_data
#			cart.add(
#				product=product,
#				quantity=cd['quantity'],
#				update_quantity=cd['update'])
#
#			return redirect('products:detail', id=product.id)
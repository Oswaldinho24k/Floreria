from django.shortcuts import render
from django.views.generic import View

class Landing (View):
	def get (self, request):
		template = 'landing.html'
		return render (request, template)

# Create your views here.

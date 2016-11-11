from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
class Main(View):
	def get(self, request):
		template='editor.html'

		return render(request, template)



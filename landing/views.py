from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def landing(request):
	form = SubscriberForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		data = form.cleaned_data
		print(data)
		new_form = form.save()
	return render(request, 'landing/landing.html', locals())

def home(request):
	form = SubscriberForm(request.POST or None)
	products_images = ProductImage.objects.filter(is_active=True, is_main=True)
	return render(request, 'home.html', locals())
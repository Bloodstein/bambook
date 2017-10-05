from django.shortcuts import render

def landing(request):
	name = "BAMbook"
	current_date = "05.10.2017"
	return render(request, 'landing/landing.html', locals())
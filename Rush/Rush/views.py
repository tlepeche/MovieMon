from django.shortcuts import render
from .set import load_settings
from django.http import Http404


# Create your views here.

def titleScreen(request):
	try:
		load_settings()
	except Exception as e:
		raise Http404(e)
	return render(request, 'Moviemon/Titlescreen.html')

def worldmap(request):
	return render(request, 'Moviemon/worldmap.html')

def battle(request):
	return HttpResponse("A FAIRE")

def options(request):
	return render(request, 'Moviemon/options.html')

def save(request):
	return render(request, 'Moviemon/save.html')

def	load(request):
	return render(request, 'Moviemon/load.html')

def moviedex(request):
	pass


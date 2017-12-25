from django.http import HttpResponse
from .models import Poster
from django.template import loader
from django.shortcuts import render

def index (request):
	all_poster = Poster.objects.all()
	context ={'all_poster' : all_poster}
	return render(request, 'poster_app/index.html', context)

def opportunities(request, poster_opportunities):
	return HttpResponse('<h1>Poster dated on </h1>' + str(poster_opportunities))

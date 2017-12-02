from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

def index (request):
    return HttpResponse('Poster_App_Template_HTML_Layout.html')

from django.shortcuts import render
from django.http import HttpResponse # You can use this for simple text responses

def index(request):
    """
    Handles requests for the app's home page and renders the template.
    """
    return render(request, 'index.html' )
# Create your views here.

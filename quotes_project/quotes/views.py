from django.shortcuts import render
from .models import Quote, Tag, Author


def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/home.html', {"quotes": quotes})


def register(request):
    return render(request, 'quotes/home.html')

def add_author(request):
    return render(request, 'quotes/home.html')

def add_quote(request):
    return render(request, 'quotes/home.html')

def add_tag(request):
    return render(request, 'quotes/home.html')

def quotes_by_tag(request):
    return render(request, 'quotes/home.html')

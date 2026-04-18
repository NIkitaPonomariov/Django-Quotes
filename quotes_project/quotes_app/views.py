from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote, Author



def main(request):
    #firs we need get all values from db
    quotes = Quote.objects.all()
    return render(request, 'quotes_app/main.html',  {"quotes":quotes})


def about_author(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes_app/about.html', {"author":author})
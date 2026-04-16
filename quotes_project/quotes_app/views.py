from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote



def main(request):
    #firs we need get all values from db
    quotes = Quote.objects.all()
    return render(request, 'quotes_app/main.html',  {"quotes":quotes})


def author_page(request, author_id):
    return render(...) # here code tomorrow!
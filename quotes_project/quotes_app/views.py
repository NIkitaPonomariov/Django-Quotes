from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote, Author
from django.contrib.auth.forms import UserCreationForm

def main(request):
    #firs we need get all values from db
    quotes = Quote.objects.all()
    return render(request, 'quotes_app/main.html',  {"quotes":quotes})


def about_author(request, author_id):
    #here we take author and in our template we show all info
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes_app/about.html', {"author":author})

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'quotes_app/register.html', {'form': form})



def add_():
    pass

def add_():
    pass

def add_():
    pass 
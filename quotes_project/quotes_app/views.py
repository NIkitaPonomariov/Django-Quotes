from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote, Author
from django.contrib.auth.forms import UserCreationForm
from .forms import QuoteForm


def main(request):
    #firs we need get all values from db
    posts = Quote.objects.all()
    per_page = 10
    paginator = Paginator(posts, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quotes_app/main.html',  {"page_obj":page_obj})


def about_author(request, author_id):
    #here we take author and in our template we show all info
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes_app/about.html', {"author":author})

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('quotes_app:login')

    return render(request, 'quotes_app/register.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = QuoteForm()

    return render(request, "quotes_app/quote.html", {"form": form})


def add_():
    pass

def add_():
    pass 
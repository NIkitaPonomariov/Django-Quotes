from django.shortcuts import render
from .models import Quote, Tag, Author
from django.core.paginator import Paginator


def main(request):
    quote_list = Quote.objects.all().order_by('-id')
    paginator = Paginator(quote_list, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return render(request, 'quotes/home.html', {"page_obj": page_obj})


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

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author.html', {"author": author})
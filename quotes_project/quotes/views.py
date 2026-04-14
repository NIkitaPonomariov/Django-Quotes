from django.shortcuts import render, redirect
from .models import Quote, Tag, Author
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def main(request):
    quote_list = Quote.objects.all().order_by('-id')
    paginator = Paginator(quote_list, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return render(request, 'quotes/home.html', {"page_obj": page_obj})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()

    return render(request, 'quotes/register.html', {"form": form})

@login_required
def add_quote(request):
    if request.method == "POST":
        text = request.POST.get("text")
        author_id = request.POST.get("author")
        tag_name = request.POST.get("tag")

        author = Author.objects.get(id=author_id)

        quote = Quote.objects.create(
            text=text,
            author=author
        )

        tag, created = Tag.objects.get_or_create(tag=tag_name)
        quote.tags.add(tag)

    authors = Author.objects.all()
    return render(request, 'quotes/add_quote.html', {"authors": authors})

@login_required
def add_tag(request):
    return render(request, 'quotes/home.html')

def quotes_by_tag(request):
    return render(request, 'quotes/home.html')

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'quotes/author.html', {"author": author})

@login_required
def add_author(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        born_date = request.POST.get("born_date")
        born_location = request.POST.get("born_location")
        description = request.POST.get("description")

        Author.objects.create(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )

        return redirect('/')

    return render(request, 'quotes/add_author.html')
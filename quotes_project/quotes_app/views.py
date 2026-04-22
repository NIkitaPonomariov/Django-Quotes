from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from django.contrib.auth.forms import UserCreationForm
from .forms import QuoteForm, TagForm, AuthorForm
from django.db.models import Count
import requests
from bs4 import BeautifulSoup
from django.contrib import messages


def main(request):
    #firs we need get all values from db
    posts = Quote.objects.all()
    per_page = 10
    paginator = Paginator(posts, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_ten_tags = (
        Tag.objects
        .annotate(num_quotes=Count('quote'))
        .order_by('-num_quotes')[:10]
        )
    
    return render(
        request, 
        'quotes_app/main.html',  
        {"page_obj":page_obj,
         "top_tags": top_ten_tags}
        )


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

@login_required
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TagForm()
    
    return render(request, "quotes_app/tag.html", {"form":form})
    
@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()
    
    return render(request, "quotes_app/author.html", {"form":form})



def by_tag(request, tag):
    quotes_with_tag = Quote.objects.filter(tags__tag=tag)

    return render(
        request,
        "quotes_app/by_tag.html",
        context={"quotes_with_tag": quotes_with_tag, "tag_id": tag}
    )


def scrape_data_from_cite(request):
    #get data
    try:    
        quotes, links = parse_quotes()
        authors = parse_authors(links)
    except Exception:
        return redirect('/')

    #save authors
    for author_data in authors:
        Author.objects.get_or_create(
            fullname=author_data["fullname"],
            defaults={
                "born_date": author_data["born_date"],
                "born_location": author_data["born_location"],
                "description": author_data["description"],
            }
        )

    #save quotes 
    for q in quotes:
        author = Author.objects.filter(fullname=q["author"]).first()

        if author and not Quote.objects.filter(text=q["quote"]).exists():
            quote = Quote.objects.create(
                text=q["quote"],
                author=author
            )

            for tag_name in q["tags"]:
                tag, _ = Tag.objects.get_or_create(tag=tag_name)
                quote.tags.add(tag)
    #send message 
    messages.success(request, "Scraping completed!")
    #back home
    return redirect(to='/')




"""
here functions from my last homework with parcing data from quotesto scrape
i just pu it here and use couse its cool)
"""

BASE_URL = "https://quotes.toscrape.com/"

def parse_authors(links: set[str]) -> list[dict]:
    authors_data = []
    for link in links:
        url = BASE_URL + link
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        fullname = soup.find("h3", class_ = "author-title").text.strip()
        born_date = soup.find("span", class_ = "author-born-date").text
        born_location = soup.find("span", class_ = "author-born-location").text
        description = soup.find("div", class_ = "author-description").text.strip()

        authors_data.append({
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": description,
            })
    return authors_data



def parse_quotes() -> tuple[list[dict], set[str]]:
    quotes_data = []
    url = BASE_URL
    authors_links = set()


    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for quote in quotes:
            #find all elements for quote

            tags = quote.find_all("a", class_ = "tag")
            author = quote.find("small", class_ = "author").text
            text = quote.find("span", class_ = "text").text
            #and for authors
            link_tag = quote.find("a")
            if link_tag:
                link = link_tag.get("href")
                authors_links.add(link)

            #save data in list like a dict

            quotes_data.append({
            "tags": [tag.text for tag in tags],
            "author": author,
            "quote": text
                    })
            
            
            

        next_page = soup.find("li", class_="next")

        if next_page:
            url = BASE_URL + next_page.find("a")["href"]
        else:
            url = None

    return quotes_data, authors_links
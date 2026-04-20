import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "quotes_project.settings")
django.setup()

from quotes_app.models import Author, Tag, Quote

def load_authors():
    with open("authors.json", "r", encoding="utf-8") as f:
        authors = json.load(f)

        for item in authors:
            Author.objects.get_or_create(
                fullname=item["fullname"],
                defaults={
                    "born_date": item.get("born_date"),
                    "born_location": item.get("born_location"),
                    "description": item.get("description"),
                },
            )

    print("Authors loaded")

def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)

        for quote in quotes:
            try:
                author = Author.objects.get(fullname=quote["author"])
            except Author.DoesNotExist:
                print(f"Author not found: {quote['author']}")
                continue

            quote_obj = Quote.objects.create(
                text=quote["quote"],
                author=author
            )

            for tag_name in quote["tags"]:
                tag, _ = Tag.objects.get_or_create(tag=tag_name)
                quote_obj.tags.add(tag)

    print("Quotes loaded")


if __name__ == "__main__":
    load_authors()
    load_quotes()
    print("DONE ")
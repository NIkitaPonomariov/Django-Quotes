from django.forms import ModelForm
from .models import Quote, Tag, Author

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author", "tags"]
        #now models has text author and tags fiel)


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["tag"]


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["fullname","born_date","born_location","description"]
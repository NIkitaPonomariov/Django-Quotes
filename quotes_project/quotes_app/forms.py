from django.forms import ModelForm
from .models import Quote

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ["text", "author", "tags"]
        #now models has text author and tags fiel)
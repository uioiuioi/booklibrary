from django import forms
from django.forms.models import ModelForm
from .models import Book
from django import forms

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'detail', 'rank')

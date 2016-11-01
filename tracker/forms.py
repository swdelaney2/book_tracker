from django import forms
from django.forms import ModelForm
from .models import Book

class NewBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'image', 'google_id', 'read']
        # widgets = {'title': forms.HiddenInput()}

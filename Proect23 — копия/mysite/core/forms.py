from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Contr_ID', 'pdf', 'ContrN', 'Uch_ID', 'AttachType', 'Attachimage', 'AttachDate', 'MainAttach_ID', 'Note','Status','EditDate')

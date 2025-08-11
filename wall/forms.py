from django import forms
from .models import Note



class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ['title', 'content', 'color','due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Content'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            
        }
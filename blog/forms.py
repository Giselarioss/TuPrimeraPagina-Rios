from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del autor'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'image']  # Agrega 'image'
        widgets = {
            # ... (widgets existentes)
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Agrega widget para el campo
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar por título de post', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el título'}))
   
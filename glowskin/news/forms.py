from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import User
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название статьи"
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс статьи"
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата публикации",
                'type': 'date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст статьи"
            }),
        }


class UserRegistrateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password']

        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя пользователя"
            }),
            "last_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Фамилия"
            }),
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя"
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Почта",
            }),
            "password": forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': "Пароль",
            })
        }

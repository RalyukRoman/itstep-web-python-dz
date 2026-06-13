from django import forms
from .models import AppReview, BookReview


class AppReviewModelForm(forms.ModelForm):
    class Meta:
        model = AppReview
        fields = ['nickname', 'email', 'stars', 'experience']

        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш нік', 'minlength': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'}),
            'stars': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class BookReviewModelForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['nickname', 'rating', 'review_text', 'has_spoilers']

        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш нік'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'review_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'has_spoilers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
from django.shortcuts import render
from .forms import AppReviewModelForm, BookReviewModelForm
from .models import AppReview, BookReview


def app_reviews(request):
    """Вивід відгуків на додатки та форми для додавання нового відгуку"""
    
    app_form = AppReviewModelForm()
    app_review = AppReview.objects.order_by('-id')

    if request.method == 'POST':
        if 'submit_app' in request.POST:
            app_form = AppReviewModelForm(request.POST)
            if app_form.is_valid():
                app_form.save()
                app_form = AppReviewModelForm()
                app_review = AppReview.objects.order_by('-id')

    return render(request, 'reviews/app_dashboard.html', {
        'app_form': app_form,
        'app_reviews': app_review,
    })


def book_reviews(request):
    """Вивід відгуків на книги та форми для додавання нового відгуку"""

    book_form = BookReviewModelForm()
    book_review = BookReview.objects.order_by('-id')

    if request.method == 'POST':
        if 'submit_book' in request.POST:
            book_form = BookReviewModelForm(request.POST)
            if book_form.is_valid():
                book_form.save()
                book_form = BookReviewModelForm()
                book_review = BookReview.objects.order_by('-id')

    return render(request, 'reviews/book_dashboard.html', {
        'book_form': book_form,
        'book_reviews': book_review,
    })

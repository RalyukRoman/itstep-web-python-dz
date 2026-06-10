from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Writer, Book


def index(request):
    """Головна сторінка."""

    path = 'main/index.html'
    return render(request, path)


def _get_books_by_writer_and_year(request, writer_slug, year):
    """Внутрішня логіка фільтрації книг за автором та роком."""

    writer = Writer.objects.filter(slug=writer_slug).first()
    if not writer:
        return redirect('writers_list')
    
    books = Book.objects.filter(writer=writer, publication_year=year)
    if not books.exists():
        return redirect('writer_detail', writer_slug=writer.slug)
    
    context = { 'writer': writer, 'year': year, 'books': books }
    path = 'main/writer_year_books.html'
    return render(request, path, context)


def _get_all_writers(request):
    """Внутрішня логіка для відображення повного списку письменників."""

    writers = Writer.objects.all()

    context = { 'writers': writers }
    path = 'main/writers_list.html'
    return render(request, path, context)


def writers_list(request):
    """
        Аналізує URL і викликає потрібну підфункцію: 
        повний список письменників або книги за автором та роком.
    """

    writer_slug = request.GET.get('writers')
    year = request.GET.get('year')

    if writer_slug and year:
        return _get_books_by_writer_and_year(request, writer_slug, year)

    return _get_all_writers(request)


def writer_detail(request, writer_slug):
    """Детальна інформація про конкретного письменника."""

    try:
        writer = get_object_or_404(Writer, slug=writer_slug)
        books = writer.books.all()

        context = { 'writer': writer, 'books': books }
        path = 'main/writer_detail.html'
        return render(request, path, context)
    
    except Http404:
        return redirect('writers_list')


def writer_book_detail(request, writer_slug, book_slug):
    """Детальна інформація про конкретну книгу конкретного письменника."""
    
    try:
        writer = get_object_or_404(Writer, slug=writer_slug)
        book = get_object_or_404(Book, writer=writer, slug=book_slug)

        context = { 'book': book }
        path = 'main/book_detail.html'
        return render(request, path, context)
    
    except Http404:
        return redirect('writer_detail', writer_slug=writer_slug)


def books_top(request, undefined=None):
    """Список усіх книг у топі."""

    if undefined is not None:
        return redirect('books_top')
    
    books = Book.objects.filter(top_place__isnull=False)

    context = { 'books': books }
    path = 'main/books_top.html'
    return render(request, path, context)


def book_detail(request, book_place):
    """Детальна інформація про конкретну книгу за місцем в топі."""
    
    try:
        book = get_object_or_404(Book, top_place=book_place)

        context = { 'book': book }
        path = 'main/book_detail.html'
        return render(request, path, context)
    
    except Http404:
        return redirect('books_top')

from django.shortcuts import render

from .services import (
    get_news,
    get_management,
    get_facts,
    get_history_people,
    get_history_photos
)


def index_view(request):
    """Відображає головну сторінку сайту"""
    path = 'main/index.html'
    return render(request, path)


def news_view(request):
    """Відображає сторінку з новинами про місто"""
    list_of_news = get_news()

    path = 'main/news.html'
    context = { 'list_of_news': list_of_news }
    return render(request, path, context)


def management_view(request):
    """Відображає сторінку з офіційними особами міста"""
    management = get_management()

    path = 'main/management.html'
    context = { 'list_of_officials': management }
    return render(request, path, context)


def facts_view(request):
    """Відображає сторінку з цікавими фактами про місто"""
    list_of_facts = get_facts()

    path = 'main/facts.html'
    context = { 'list_of_facts': list_of_facts }
    return render(request, path, context)


def contacts_view(request):
    """Відображає сторінку з контактними інформацією"""
    path = 'main/contacts.html'
    return render(request, path)


def history_view(request):
    """Відображає сторінку з інформацією про історію міста"""
    path = 'main/history.html'
    return render(request, path)


def history_people_view(request):
    """Відображає сторінку з історичними постатами"""
    history_people = get_history_people()

    path = 'main/history_people.html'
    context = { 'people': history_people }
    return render(request, path, context)


def history_photos_view(request):
    """Відображає сторінку з історичними фотографіями міста."""
    history_photos = get_history_photos()

    path = 'main/history_photos.html'
    context = { 'photos': history_photos }
    return render(request, path, context)
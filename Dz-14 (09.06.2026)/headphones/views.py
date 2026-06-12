from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Headphone


def headphone_detail(request):
    """Аналізує URL і повертає відповідну модель навушників."""

    model_slug = request.GET.get('model')

    if not model_slug:
        raise Http404("Параметр 'model' не вказано")

    headphone = get_object_or_404(
        Headphone, slug=model_slug
    )

    context = { 'headphone': headphone }
    path = 'headphones/detail.html'
    return render(request, path, context)
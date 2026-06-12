from django.shortcuts import render, redirect
from .models import CarBrand


def cars_main(request):
    """Головна сторінка."""
    path = 'cars/main.html'
    return render(request, path)


def car_brand(request, car_brand_slug):
    """Сторінка для відображення інформації об автомобільному бренді."""

    brand = CarBrand.objects.filter(
        slug=car_brand_slug
    ).first()
    
    if not brand:
        return redirect('cars_main')
    
    context = { 'brand': brand }
    path = 'cars/brand.html'
    return render(request, path, context)

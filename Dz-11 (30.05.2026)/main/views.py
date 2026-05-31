from django.shortcuts import render
from datetime import datetime

from .services import (
    get_multiplication_matrix,
    calculate_programmer_day,
)

def home_view(request):
    path = 'main/home.html'
    return render(request, path)

def task_3_view(request):
    path = 'main/current_time.html'
    return render(request, path)

def task_4_view(request):
    matrix = get_multiplication_matrix()

    path = 'main/multiplication_table.html'
    context = { 'table_data': matrix }
    return render(request, path, context)

def task_5_view(request):
    current_year = datetime.now().year
    date = calculate_programmer_day(current_year)

    path = 'main/programmer_day.html'
    context = { 'date': date }
    return render(request, path, context)
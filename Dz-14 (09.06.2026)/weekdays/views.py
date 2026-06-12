from django.shortcuts import render, get_object_or_404
from .models import Weekday
from datetime import datetime


def current_day(request):
    """Сторінка для відображення інформації про поточний день тижня."""

    current_day_id = datetime.today().weekday() + 1

    day_info = get_object_or_404(
        Weekday, id=current_day_id
    )
    
    context = { 'day': day_info }
    path = 'weekdays/day.html'
    return render(request, path, context)

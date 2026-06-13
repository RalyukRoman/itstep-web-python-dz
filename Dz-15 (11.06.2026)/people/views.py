from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import PersonSearchForm
from .models import Person


def search_people(request):
    form = PersonSearchForm(request.GET or None)
    results = Person.objects.all()

    if form.is_valid():
        full_name = form.cleaned_data.get('full_name')
        city = form.cleaned_data.get('city')

        if full_name:
            results = results.filter(
                full_name__icontains=full_name
            )
            
        if city:
            results = results.filter(
                city__icontains=city
            )

    paginator = Paginator(results, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']

    return render(request, 'people/search.html', {
        'form': form,
        'page_obj': page_obj,
        'query_params': query_params.urlencode(),
    })
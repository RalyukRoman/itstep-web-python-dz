from django.contrib import admin

from .models import (
    News,
    CityOfficial,
    Fact,
    HistoricalPeople,
    HistoricalPhoto
)


admin.site.register(News)
admin.site.register(CityOfficial)
admin.site.register(Fact)
admin.site.register(HistoricalPeople)
admin.site.register(HistoricalPhoto)
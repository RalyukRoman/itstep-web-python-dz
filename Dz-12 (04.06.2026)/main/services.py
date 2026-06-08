from .models import News, CityOfficial, Fact, HistoricalPhoto, HistoricalPeople


def get_news():
    """Отримує всі новини, відсортовані за датою публікації"""
    return News.objects.all().order_by('-pub_date')


def get_management():
    """Отримує список офіційних осіб міста"""
    return CityOfficial.objects.all()


def get_facts():
    """Отримує цікаві факти про місто"""
    return Fact.objects.all()


def get_history_people():
    """Отримує список видатних історичних постатей"""
    return HistoricalPeople.objects.all()


def get_history_photos():
    """Отримує всі історичні фотографії"""
    return HistoricalPhoto.objects.all()

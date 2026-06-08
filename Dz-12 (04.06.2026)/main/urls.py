from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),

    path('news/', views.news_view, name='news'),
    path('management/', views.management_view, name='management'),
    path('facts/', views.facts_view, name='facts'),
    path('contacts/', views.contacts_view, name='contacts'),

    path('history/', views.history_view, name='history'),
    path('history/people/', views.history_people_view, name='history_people'),
    path('history/photos/', views.history_photos_view, name='history_photos'),
    

    path('news/<path:undefined>/', views.news_view),
    path('management/<path:undefined>/', views.management_view),
    path('facts/<path:undefined>/', views.facts_view),
    path('contacts/<path:undefined>/', views.contacts_view),

    path('history/<path:undefined>/', views.history_view),
    path('history/people/<path:undefined>/', views.history_people_view),
    path('history/photos/<path:undefined>/', views.history_photos_view),

    path('<path:undefined>', views.index_view),
]
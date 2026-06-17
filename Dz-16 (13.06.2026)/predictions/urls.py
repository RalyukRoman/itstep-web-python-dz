from django.urls import path
from . import views


urlpatterns = [
    path('prediction/random/', views.get_random_prediction, name='get_random_prediction')
]
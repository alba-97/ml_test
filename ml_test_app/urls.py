from django.urls import path
from .views import IsMutant, StatsView

urlpatterns = [
    path('mutant', IsMutant.as_view(), name='mutant'),
    path('stats', StatsView.as_view(), name='stats'),
]
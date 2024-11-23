from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.getCompetitions),
    path('<str:competition_code>/teams/', views.getTeams),
    path('teams/', views.getTeams),
    path('<str:competition_code>/matches/', views.getMatches),
    path('matches/', views.getMatches),
    path('<str:competition_code>/standings/', views.getStandings),
    path('standings/', views.getStandings),
]
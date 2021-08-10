from django.urls import path
from . import views

urlpatterns = [
    path('', views.scoreboardOverview, name="api-overview"),
    path('/scores', views.scores, name="highscores"),
  ]
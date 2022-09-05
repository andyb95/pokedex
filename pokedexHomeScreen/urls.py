from django.urls import path
from . import views

app_name = 'pokedex'
urlpatterns = [
    path('', views.index, name='index'),
    path('catchPokemon/', views.catchPokemon, name='catchPokemon'),
    path('caughtPokemon/', views.caughtPokemon, name='caughtPokemon'),
    path('<int:pk>/releasePokemon/', views.releasePokemon, name='releasePokemon'),
    path('<int:pk>/renamePokemon/', views.renamePokemon, name='renamePokemon'),
]
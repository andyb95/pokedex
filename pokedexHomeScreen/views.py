from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pokemon
import requests
import random

def index(request):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random.randint(1, 150)}')
    wildPokemonData = response.json()

    return render(request, 'pokedex/index.html', {
        'pokemon': {
            'name': wildPokemonData['name'].capitalize(),
            'image': wildPokemonData['sprites']['other']['official-artwork']['front_default'],
        }
    })

def catchPokemon(request):
    wildPokemon = eval(request.POST.get('catchPokemon'))
    caughtPokemon = Pokemon(
        name = wildPokemon['name'],
        image = wildPokemon['image']
    )
    caughtPokemon.save()
    return HttpResponseRedirect(reverse('pokedex:index'))

def caughtPokemon(request):
    caughtPokemon = Pokemon.objects.all()
    return render(request, 'pokedex/caughtPokemon.html', { 'caughtPokemon': caughtPokemon })

def releasePokemon(request, pk):
    pokemon = Pokemon(pk)
    pokemon.delete()
    return HttpResponseRedirect(reverse('pokedex:caughtPokemon'))

def renamePokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    newName = request.POST.get('renamePokemon')
    pokemon.name = newName
    pokemon.save()
    return HttpResponseRedirect(reverse('pokedex:caughtPokemon'))

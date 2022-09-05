from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pokemon
import requests
import random

def index(request):
    # return render(request, 'index.html')
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
    print(wildPokemon['name'])
    caughtPokemon = Pokemon(
        name = wildPokemon['name'],
        image = wildPokemon['image'],
        caught = True
    )
    try:
        caughtPokemon.save()
    except (KeyError, caughtPokemon.id.DoesNotExist):
        return render(request, 'pokedex/index.html'), {
            'error_message': "{% wildPokemon.name %} got away"
        }
    else:
        return HttpResponseRedirect(reverse('pokedex:index'))

def caughtPokemon(request):
    try:
        caughtPokemon = Pokemon.objects.all()
    except (KeyError, caughtPokemon.DoesNotExist):
        return render(request, 'pokedex/index.html', {
            'error_message': "You gotta catch some pokemon!"
        })
    else:
        print(caughtPokemon)
        return render(request, 'pokedex/caughtPokemon.html', { 'caughtPokemon': caughtPokemon })

def releasePokemon(request, pk):
    pokemon = Pokemon(pk)
    pokemon.delete()
    return HttpResponseRedirect(reverse('pokedex:caughtPokemon'))

def renamePokemon(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    print(pokemon)
    newName = request.POST.get('renamePokemon')
    pokemon.name = newName
    print(pokemon.name)
    pokemon.save()
    # try: 
    # except (KeyError, pokemon.DoesNotExist):
    #     return render(request, 'pokedex/index.html'), {
    #         'error_message': "{% pokemon.name %} doesn't like the nickname"
    #     }
    # else:
    return HttpResponseRedirect(reverse('pokedex:caughtPokemon'))

# def result(request):
#     result = request.GET['result']
#     return render(request)

# def wildPokemon(request):
#     return HttpResponse("Here are three pokemon")

# def caughtPokemon(request):
#     return HttpResponse("Here are the pokemon you've caught")

# def encounteredPokemon(request):
#     return HttpResponse("Here are the Pokemon you've seen")

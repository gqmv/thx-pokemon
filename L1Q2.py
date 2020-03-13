# Obtém o valor de entrada do usuário
codigo_pokemon = int(input())

# Determina qual pokemon for escolhido com base em codigo_pokemon
if codigo_pokemon == 1:
    nome_pokemon = "Bulbassauro"
elif codigo_pokemon == 2:
    nome_pokemon = "Ivyssauro"
elif codigo_pokemon == 3:
    nome_pokemon = "Venossauro"
elif codigo_pokemon == 4:
    nome_pokemon = "Charmander"
elif codigo_pokemon == 5:
    nome_pokemon = "Charmeleon"
elif codigo_pokemon == 6:
    nome_pokemon = "Charizard"
elif codigo_pokemon == 7:
    nome_pokemon = "Squirtle"
elif codigo_pokemon == 8:
    nome_pokemon = "Wartortle"
elif codigo_pokemon == 9:
    nome_pokemon = "Blastoise"
elif codigo_pokemon == 10:
    nome_pokemon = "Caterpie"
elif codigo_pokemon == 11:
    nome_pokemon = "Metapod"
elif codigo_pokemon == 12:
    nome_pokemon = "Butterfree"
else:
    nome_pokemon = "Pokemon invalido no momento"

# Informa o resultado ao usuario
print(nome_pokemon)
# Obtem o valor de entrada do usuario
numero_escolhido = int(input())

# Determina qual o pokemon escolhido, tomando como base numero_escolhido
if numero_escolhido == 1:
    pokemon_escolhido = "Bulbassauro"
elif numero_escolhido == 2:
    pokemon_escolhido = "Charmander"
else:
    pokemon_escolhido = "Squirtle"

# Informa ao usuario o resultado
print(pokemon_escolhido)
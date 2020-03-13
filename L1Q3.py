# Obtem o valor de entrada do usuário
identificador_treinador = input()

# Dado indentificador_pokemon , obtém o pokemon escolhido
codigo_pokemon = identificador_treinador[6]
nome_pokemon = None
if codigo_pokemon == "b":
    nome_pokemon = "Bulbassauro"
elif codigo_pokemon == "c":
    nome_pokemon = "Charmander"
elif codigo_pokemon == "s":
    nome_pokemon = "Squirtle"
else:
    print("Codigo Invalido")

# Informa ao usuário o resultado
if nome_pokemon != None:
    print(nome_pokemon)
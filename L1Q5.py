# Obtem os valores de entrada do usuario
entrada = input()
ataques = entrada.split()
# ataque1 = int(ataques[0])
# ataque2 = int(ataques[1])
# ataque3 = int(ataques[2])


# Determina se o Rattata foi derrotado
rattata_derrotado = None
condicao_tamanho = None # Refere-se a condição de um dos ataques ser maior que 10
condicao_paridade = None # Refere-se condição de um dos ataques ser par
if "0" in ataques:
    rattata_derrotado = False
else:
    for ataque in ataques: # Verifica a condicao_tamanho
        if int(ataque) > 10:
            ataques.remove(ataque)
            condicao_tamanho = True
            break

    for ataque in ataques: # Verifica a condicao_paridade
        if int(ataque) % 2 == 0:
            ataques.remove(ataque)
            condicao_paridade = True
            break

    if condicao_paridade and condicao_tamanho: # Verifica se ambas as condicoes sao atendidas
        rattata_derrotado = True

# Informa o resultado ao usuário
if rattata_derrotado:
    print("Sim")
else:
    print("Nao")


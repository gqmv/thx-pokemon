# Obtem os valores de entrada dos usuarios
tipo_ataque = input()
tipo_defesa = input()

# Determina se o ataque tem vantagem
tem_vantagem = None
if tipo_ataque == "Planta":
    if tipo_defesa == "Fogo":
        tem_vantagem = False
    if tipo_defesa == "Agua":
        tem_vantagem = True

if tipo_ataque == "Fogo":
    if tipo_defesa == "Agua":
        tem_vantagem = False
    if tipo_defesa == "Planta":
        tem_vantagem = True

if tipo_ataque == "Agua":
    if tipo_defesa == "Planta":
        tem_vantagem = False
    if tipo_defesa == "Fogo":
        tem_vantagem = True

# Informa o resultado ao usuario
if tem_vantagem == True:
    print("Vantagem")
elif tem_vantagem == False:
    print("Desvantagem")
else:
    print("Empate")


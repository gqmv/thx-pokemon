
def charmander ():
    # Obtem o valor de entrada do usuário
    cp = input()

    if len(cp) != 4:
        return "Charmander derrotado"

    # Determina o valor de AB e de CD em int
    ab = cp[:2]
    ab = int(ab)
    cd = cp[2:]
    cd = int(cd)

    # Determina AB + CD
    ef = ab + cd
    cp = int(cp)

    # Verifica se a condicao e
    if cp == ef**2:
        return "Charmander vitorioso"
    else:
        return "Charmander derrotado"


if __name__ == "__main__":
    resultado = charmander()
    print(resultado)




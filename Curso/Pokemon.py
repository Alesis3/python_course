
import os
from random import randint

vida_pikachu = 80
vida_charmander = 90
vida_final_pikachu = vida_pikachu
vida_final_charmander = vida_charmander

while vida_final_pikachu > 0 and vida_final_charmander > 0:
    # Ataque de pikachu
    print("Turno de pikachu")
    ataque_pikachu = randint(1, 2)

    if ataque_pikachu == 1:
        print("Pikachu ataca con impactrueno")
        vida_final_charmander -= 10
    else:
        print("Pikachu ataca con bola")
        vida_final_charmander -= 8

    # Si la vida va a negativo que aparezca como 0
    if vida_final_charmander < 0:
        vida_final_charmander = 0

    if vida_final_pikachu < 0:
        vida_final_pikachu = 0

    # Mostrar las barras de vida de los pokemones
    barra_vd_pikachu = int(vida_final_pikachu * 10 / vida_pikachu)
    print("Pikachu: [{}]{}/{}".format("#" * barra_vd_pikachu, vida_final_pikachu, vida_pikachu),
          " " * (10 - barra_vd_pikachu))

    barra_vd_charmander = int(vida_final_charmander * 10 / vida_charmander)
    print("Charmander: [{}]{}/{}".format("#" * barra_vd_charmander, vida_final_charmander, vida_charmander),
          " " * (10 - barra_vd_charmander))

    input("Enter para continuar... \n\n")
    os.system("clear")
    ataque_charmander = None

    # Ataque de charmander solo si sigue con vida
    while (vida_final_charmander > 0
           and ataque_charmander != "A" and ataque_charmander != "B" and ataque_charmander != "C"):
        print("Turno de charmander")
        ataque_charmander = input(
            "Que ataque quieres realizar? \n"
            "[A]Arañazo Scratch \n [B]Gruñido Growl \n [C]Ascuas Ember \n[D]No hacer nada")

        # Opciones de ataque
        if ataque_charmander == "A":
            print("Charmander ataca con Arañazo Scratch")
            vida_final_pikachu -= 10
        elif ataque_charmander == "B":
            print("Charmander ataca con Gruñido Growl")
            vida_final_pikachu -= 8
        elif ataque_charmander == "C":
            print("Charmander ataca con Ascuas Ember")
            vida_final_pikachu -= 5
        elif ataque_charmander == "D":
            vida_final_pikachu -= 0

        # Si la vida va a negativo que aparezca como 0
        if vida_final_pikachu < 0:
            vida_final_pikachu = 0

        if vida_final_charmander < 0:
            vida_final_charmander = 0

        # Mostrar las barras de vida de los pokemones
        barra_vd_pikachu = int(vida_final_pikachu * 10 / vida_pikachu)
        print("Pikachu: [{}]{}/{}".format("#" * barra_vd_pikachu, vida_final_pikachu, vida_pikachu),
              " " * (10 - barra_vd_pikachu))

        barra_vd_charmander = int(vida_final_charmander * 10 / vida_charmander)
        print("Charmander: [{}]{}/{}".format("#" * barra_vd_charmander, vida_final_charmander, vida_charmander),
              " " * (10 - barra_vd_charmander))

        input("Enter para continuar ... \n\n")
        os.system("clear")

if vida_final_pikachu <= 0:
    print("Ha ganado charmander!")

else:
    print("Ha ganado pikachu!")


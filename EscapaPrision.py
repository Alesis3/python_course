import random

print("Despiertas en un cuarto vacio, atado en una cama,"
      " observas que la correa de tu mano izquierda esta floja y decides desatarte,\n"
      "en el cuarto hay una puerta que no sabes a donde lleva. \n"
      "¿Que haces? ")

desicion = input("[A]Sales del cuarto [B] Esperas en el cuarto ")

if desicion == "A":
    print("Entras a otro cuarto en donde hay 3 salidas, una escotilla, una puerta negra y ventana abierta\n"
          "¿A donde te diriges?")
    desicion = input("[A]Escotilla, [B]Puerta negra o [C]Ventana")

    if desicion == "A":
        print("Entras a un tunel y te encuentras a otra persona \n"
              "¿Haces equipo o te vas por tu cuenta")
        desicion = input("[A]Equipo, [B]Por tu cuenta")

        if desicion == "A":
            print("Siguen juntos hasta el final del tunel y se encuentran con un murcielago gigante \n"
                  "que es capas de comunicarse con ustedes por telepatia y menciona que te puede \n"
                  "ayudar a salir de ahi pero con la condicion de que dejes a la otra persona como sacrificio\n"
                  "¿Que haces?")
            desicion = input("[A]Dejas a la persona [B]Te niegas a dejarla")

            if desicion == "A":
                print("Era una prueba para demostrar tus valores y no la pasaste ¡Perdiste!")

            elif desicion == "B":
                print("pasaste la prueba y los ayuda a salir sanos y salvos, tienes otro dia que vivir \n"
                      "¡FELICIDADES!\n"
                      "Fin del jeugo")

    elif desicion == "B":
        print("Te encuentras un grupo de marcianos y te capturaron. \n"
              "Al observar que lograste desatarte deciden hacerte una prueba. \n "
              "Te piden que resuelvas la siguiente operacion matematica")

        operacion = random.randint(1, 100)
        print("23 * {}".format(operacion))
        respuesta = int(input("¿Cual es el resultado?"))

        if respuesta == 23 * operacion:
            print("Te dejaron ir. ¡Vaya! al parecer los marcianos no buscan personas inteligentes. \n "
                  "¡Felicidades! \n "
                  "Fin del juego")
        else:
            print("Al parecer no eres tan inteligente, te capturaron y veran lo que esta mal contigo \n "
                  "Perdiste")

    elif desicion == "C":
        print("Entras a un cuarto con una mesa y encima hay un cuaderno negro \n "
              "¿Te lo llevas?")
        cuaderno = False
        desicion = input("[A]Si [B]No")
        if desicion == "A":
            print("Agarras el cuaderno")
            cuaderno = True

        elif desicion == "B":
            print("No has agarrado el cuaderno")

    print("Observas que hay una escotilla que lleva a los conductos de ventilacion \n"
          "caminar por 20min por los conductos de ventilacion hasta que se empieza debilitar \n "
          "la estructura y caes en un laboratorio donde hay pociones y son dos las que te llaman la atencion \n"
          "una pocion para hacerte pequeño y otro para hacerte invisible\n"
          "¿Cual eliges?")

    desicion = input("[A]Invisible [B]Pequeño")

    if desicion == "A":
        print("Los marcianos tienen la capacidad de ver a las personas invisibles \n "
              "te descubrieron y experimentan contigo ¡PERDISTE!")

    elif desicion == "B":
        print("Puedes entrar por la cañeria y al final de esta te encuentras la salida \n "
              "pero esta resguardada por una rata que tiene la capacidad de hablar \n"
              "Te pide a cambio un objeto para dejarte pasar")

        desicion = input("¿Le das la libreta? [A]Si [B]No")

        if desicion == "A" and cuaderno == False:
            print("Tratas de engañarlo con que traes un cuaderno, te descubre y te devora \n"
                  "¡PERDISTE!")

        elif desicion == "A" and cuaderno == True:
            print("Le das el cuaderno y te deja salir \n"
                  "¡Felicidades tienes otro dia que vivir! \n"
                  "Fin del juego")

        elif desicion == "B":
            print("Por no querer darle algo se enfada y te devora \n "
                  "¡PERDISTE!")
else:
    print("Llegaron dos marcianos y experimentaron contigo, ¡PERDISTE!")

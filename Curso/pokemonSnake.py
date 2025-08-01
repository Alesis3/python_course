def juegosnake():
    import os
    import random
    import readchar

    obstacle = """\
                ####         
    #  #######           ####
    ##   ############    ####
    ## #####                 
    ##  #####  #######    ###
    #  #########            #
    #   ####          #######
    ##    #######         ###
    ####   ###    ###       #
    #####                 ###
    #########  #####         
    ######    ##########   ##
    #######               ###\
    """
    obstacle = [list(row) for row in obstacle.split("\n")]
    HEIGHT = len(obstacle)
    WIDTH = len(obstacle[0])
    MY_POSX = 0
    MY_POSY = 1
    TRAINERS = 4
    my_position = [0, 0]
    trainers = []
    battle_pokemon = False

    # genera entrenadores
    while len(trainers) < TRAINERS:
        new_trainers = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]

        if new_trainers not in trainers and new_trainers != my_position \
                and obstacle[new_trainers[MY_POSY]][new_trainers[MY_POSX]] != "#":
            trainers.append(new_trainers)

    while True:
        # genera el contorno del mapa
        print("+" + "-" * WIDTH * 3 + "+")
        for coordinate_y in range(HEIGHT):
            print("|", end="")

            for coordinate_x in range(WIDTH):

                char = " "
                trainer_defeated = None

                # pocisiona los entrenadores en el mapa
                for trainer in trainers:
                    if trainer[MY_POSX] == coordinate_x and trainer[MY_POSY] == coordinate_y:
                        char = "T"
                        trainer_defeated = trainer

                # genera el simbolo de nuestro jugador
                if my_position[MY_POSX] == coordinate_x and my_position[MY_POSY] == coordinate_y:
                    char = "@"

                    if trainer_defeated:
                        trainers.remove(trainer_defeated)
                        battle_pokemon = True

                if obstacle[coordinate_y][coordinate_x] == "#":
                    char = "#"

                print(" {} ".format(char), end="")

            print("|")
        print("+" + "-" * WIDTH * 3 + "+")

        if battle_pokemon:
            # batalla
            arbok_fn_life = 100
            arbok = arbok_fn_life

            pokemon_fn_life = [90, 100, 70, 80]
            TRAINER_BATTLE = ["PIKACHU", "CHARMANDER", "MEOWTH", "BULBASAUR"]
            life_pokemons = pokemon_fn_life
            attacks = [["Trueno", "Rayo S", "Gruñido Growl"],
                       ["Pirotecnia", "Nitrocarga", "Frustración Shadow"],
                       ["Mordizco", "Arañazo", "Juego Sucio"], ["Bomba Lodo", "Latigazo", "Latigo Cepa"]]

            # Ataque y vida de los diferentes entrenadores
            trainer_type = None
            rival_life = None
            rival_attack = None
            attack_value = []
            barra_pokemon = None

            battle = random.choice(TRAINER_BATTLE)

            if battle == "PIKACHU":
                trainer_type = TRAINER_BATTLE[0]
                rival_life = life_pokemons[0]
                rival_attack = attacks[0]
                attack_value = [15, 20, 10]
                barra_pokemon = pokemon_fn_life[0]
            elif battle == "CHARMANDER":
                trainer_type = TRAINER_BATTLE[1]
                rival_life = life_pokemons[1]
                rival_attack = attacks[1]
                attack_value = [10, 15, 8]
                barra_pokemon = pokemon_fn_life[1]
            elif battle == "MEOWTH":
                trainer_type = TRAINER_BATTLE[2]
                rival_life = life_pokemons[2]
                rival_attack = attacks[2]
                attack_value = [10, 5, 25]
                barra_pokemon = pokemon_fn_life[2]
            elif battle == "BULBASAUR":
                trainer_type = TRAINER_BATTLE[3]
                rival_life = life_pokemons[3]
                rival_attack = attacks[3]
                attack_value = [10, 12, 12]
                barra_pokemon = pokemon_fn_life[3]

            os.system("clear")
            print("-" * 4 + "Te enfrentaras al temible {}".format(trainer_type) + "-" * 4)

            # batalla pokemon
            while arbok > 0 and rival_life > 0:

                # turno del pokemon rival
                print("Turno de {}".format(trainer_type))
                attack = random.randint(1, 3)
                attack_turn = None

                if attack == 1:
                    attack_turn = rival_attack[0]
                    arbok -= attack_value[0]
                elif attack == 2:
                    attack_turn = rival_attack[1]
                    arbok -= attack_value[1]
                else:
                    attack_turn = rival_attack[2]
                    arbok -= attack_value[2]

                # Si la vida es negativo se muestra en 0
                if rival_life < 0:
                    rival_life = 0
                if arbok < 0:
                    arbok = 0
                print("{} ataca con {}".format(trainer_type, attack_turn))

                barra_vd_arbok = int(arbok * 10 / arbok_fn_life)
                print("La vida de arbok es: [{}]{}/{}".format("#" * barra_vd_arbok, arbok, arbok_fn_life),
                      " " * (10 - barra_vd_arbok))

                barra_vd_rival = int(rival_life * 10 / barra_pokemon)
                print("Vida de {} es: [{}]{}/{}".format(trainer_type, "#" * barra_vd_rival, int(rival_life),
                                                        barra_pokemon))

                input("Enter para continuar...")
                os.system("clear")

                player_attack = None

                while arbok > 0 and player_attack != "A" and player_attack != "B" and player_attack != "C":

                    # Turno del jugador
                    player_attack = input("Que ataque deseas realizar? \n"
                                          "[A]Acido, \n [B]Onda Toxica,\n [C]Cola Dragon, \n\n")

                    arbok_attacks = ["Acido", "Onda Toxica", "Cola Dragon"]
                    arbok_attack = None

                    if player_attack == "A":
                        arbok_attack = arbok_attacks[0]
                        rival_life -= 10
                    elif player_attack == "B":
                        arbok_attack = arbok_attacks[1]
                        rival_life -= 20
                    elif player_attack == "C":
                        arbok_attack = arbok_attacks[2]
                        rival_life -= 16

                    # Si la vida es negativo se muestra en 0
                    if rival_life < 0:
                        rival_life = 0
                    if arbok < 0:
                        arbok = 0
                    print("Arbok ataca con {}".format(arbok_attack))

                    barra_vd_arbok = int(arbok * 10 / arbok_fn_life)
                    print("La vida de arbok es: [{}]{}/{}".format("#" * barra_vd_arbok, arbok, arbok_fn_life),
                          " " * (10 - barra_vd_arbok))

                    barra_vd_rival = int(rival_life * 10 / barra_pokemon)
                    print("Vida de {} es: [{}]{}/{}".format(trainer_type, "#" * barra_vd_rival, int(rival_life),
                                                            barra_pokemon))

                    input("Enter para continuar...")
                    os.system("clear")

                    # si acabamos con el rival se reinicia vida y quitamos el rival de la lista
                    if rival_life == 0:
                        TRAINER_BATTLE.remove(trainer_type)
                        arbok = 100
                        battle_pokemon = False

            if arbok == 0:
                print("¡Perdiste! \n"
                      "Ha gando {}".format(trainer_type))
                input("Enter para continuar")

            else:
                print("¡Felicidades has ganado!")
                input("Enter para continuar")

        # si ya no hay entrenadores se sale del juego
        if not trainers:
            print("#" * 5 + "¡¡Felicidades has ganado las batallas pokemon!!" + "#" * 5)
            input("Enter para continuar")
            break

        # movimiento del jugador
        keys = readchar.readchar()
        new_position = None

        if keys == "w":
            new_position = [my_position[MY_POSX], (my_position[MY_POSY] - 1) % HEIGHT]
        if keys == "s":
            new_position = [my_position[MY_POSX], (my_position[MY_POSY] + 1) % HEIGHT]
        if keys == "d":
            new_position = [(my_position[MY_POSX] + 1) % WIDTH, my_position[MY_POSY]]
        if keys == "a":
            new_position = [(my_position[MY_POSX] - 1) % WIDTH, my_position[MY_POSY]]
        elif keys == "b":
            break

        if new_position:
            if obstacle[new_position[MY_POSY]][new_position[MY_POSX]] != "#":
                my_position = new_position

        os.system("clear")

juegosnake()

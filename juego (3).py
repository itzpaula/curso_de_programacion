def jugar_juego():
    print("Estás caminando por un bosque oscuro 🌲🌌 y encuentras dos objetos: un FÓSFORO y una LINTERNA. ¿Con cuál te quedas?")

    # --- Primera decisión: FÓSFORO o LINTERNA ---
    while True:
        primera_eleccion = input().strip().lower()
        if primera_eleccion in ["fósforo", "fosforo", "linterna"]:
            break # Salir del bucle si la elección es válida
        else:
            print("Opción no válida. Por favor, elige 'fósforo' o 'linterna'.")

    if primera_eleccion == "fósforo" or primera_eleccion == "fosforo":
        print("\nCoges el fósforo y lo enciendes 🔥. Por un instante, el bosque se ilumina… ¡y ves un gran oso grizzly! 🐻 El fósforo se apaga.")
        print("¿Quieres CORRER o ESCONDERTE detrás de un árbol? 🌳")

        # --- Segunda decisión (Fósforo): CORRER o ESCONDERTE ---
        while True:
            segunda_eleccion_fosforo = input().strip().lower()
            if segunda_eleccion_fosforo in ["correr", "esconderte"]:
                break
            else:
                print("Opción no válida. Por favor, elige 'correr' o 'esconderte'.")

        if segunda_eleccion_fosforo == "correr":
            print("\nCorres lo más rápido que puedes, esquivando árboles y ramas. El oso te persigue de cerca.")
            print("Llegas a un río caudaloso. ¿Intentas CRUZAR el río, o BUSCAS un puente cercano? 🌉")

            # --- Tercera decisión (Correr): CRUZAR o BUSCAR ---
            while True:
                tercera_eleccion_correr = input().strip().lower()
                if tercera_eleccion_correr in ["cruzar", "buscas"]:
                    break
                else:
                    print("Opción no válida. Por favor, elige 'cruzar' o 'buscas'.")

            if tercera_eleccion_correr == "cruzar":
                print("\nTe lanzas al río. La corriente es fuerte y te arrastra. Con mucho esfuerzo, logras llegar a la otra orilla, empapado pero a salvo del oso.")
                print("Encuentras un pequeño sendero. ¿LO SIGUES o DESCANSAS para recuperar fuerzas? 😴")

                # --- Cuarta decisión (Cruzar): LO SIGUES o DESCANSAS ---
                while True:
                    cuarta_eleccion_cruzar = input().strip().lower()
                    if cuarta_eleccion_cruzar in ["lo sigues", "descansas"]:
                        break
                    else:
                        print("Opción no válida. Por favor, elige 'lo sigues' o 'descansas'.")

                if cuarta_eleccion_cruzar == "lo sigues":
                    print("\nSigues el sendero y llegas a una cabaña acogedora. ¡Felicidades, has encontrado refugio!")
                    print("FIN DEL JUEGO. ¡GANASTE! 🎉")
                elif cuarta_eleccion_cruzar == "descansas":
                    print("\nDecides descansar. Te quedas dormido y el oso finalmente te encuentra. No es un buen final.")
                    print("FIN DEL JUEGO. ¡PERDISTE! 💀")

            elif tercera_eleccion_correr == "buscas":
                print("\nBuscas un puente, pero el oso te alcanza antes de que puedas encontrar uno. No hay escapatoria.")
                print("FIN DEL JUEGO. ¡PERDISTE! 💀")

        elif segunda_eleccion_fosforo == "esconderte":
            print("\nTe escondes rápidamente detrás de un árbol grueso. El oso gruñe y olfatea cerca, pero no te ve.")
            print("Escuchas al oso alejarse. ¿Qué haces ahora? ¿ESCAPAS en silencio o BUSCAS algo de comida? 🍎")

            # --- Tercera decisión (Esconderte): ESCAPAS o BUSCAS ---
            while True:
                tercera_eleccion_esconderte = input().strip().lower()
                if tercera_eleccion_esconderte in ["escapas", "buscas"]:
                    break
                else:
                    print("Opción no válida. Por favor, elige 'escapas' o 'buscas'.")

            if tercera_eleccion_esconderte == "escapas":
                print("\nEscapas en silencio, con el corazón latiéndote a mil. Logras salir del bosque y encontrar un camino seguro.")
                print("FIN DEL JUEGO. ¡GANASTE! 🎉")
            elif tercera_eleccion_esconderte == "buscas":
                print("\nComienzas a buscar comida, haciendo ruido sin querer. El oso, que no se había ido tan lejos, te escucha y regresa.")
                print("FIN DEL JUEGO. ¡PERDISTE! 💀")

    elif primera_eleccion == "linterna":
        print("\nEnciendes la linterna 💡 y ves un camino iluminado. De pronto, oyes algo entre los árboles 🌿.")
        print("¿Quieres SEGUIR el camino o BUSCAR entre los árboles lo que hizo el ruido? 🔍")

        # --- Segunda decisión (Linterna): SEGUIR o BUSCAR ---
        while True:
            segunda_eleccion_linterna = input().strip().lower()
            if segunda_eleccion_linterna in ["seguir", "buscar"]:
                break
            else:
                print("Opción no válida. Por favor, elige 'seguir' o 'buscar'.")

        if segunda_eleccion_linterna == "seguir":
            print("\nSigues el camino iluminado. La luz de tu linterna te guía a través de la oscuridad.")
            print("Más adelante, el camino se divide en tres: uno a la IZQUIERDA, otro a la DERECHA y uno RECTO. ¿Cuál tomas? ⬅️➡️⬆️")

            # --- Tercera decisión (Seguir): IZQUIERDA, DERECHA o RECTO ---
            while True:
                tercera_eleccion_seguir = input().strip().lower()
                if tercera_eleccion_seguir in ["izquierda", "derecha", "recto"]:
                    break
                else:
                    print("Opción no válida. Por favor, elige 'izquierda', 'derecha' o 'recto'.")

            if tercera_eleccion_seguir == "izquierda":
                print("\nTomas el camino de la izquierda. Te lleva a un acantilado. No hay salida.")
                print("FIN DEL JUEGO. ¡PERDISTE! 💀")
            elif tercera_eleccion_seguir == "derecha":
                print("\nTomas el camino de la derecha. Descubres una cueva misteriosa. ¿ENTRAS o LA IGNORAS? 🦇")

                # --- Cuarta decisión (Derecha): ENTRAS o LA IGNORAS ---
                while True:
                    cuarta_eleccion_derecha = input().strip().lower()
                    if cuarta_eleccion_derecha in ["entras", "la ignoras"]:
                        break
                    else:
                        print("Opción no válida. Por favor, elige 'entras' o 'la ignoras'.")

                if cuarta_eleccion_derecha == "entras":
                    print("\nEntras a la cueva y encuentras un antiguo mapa del tesoro. ¡Qué hallazgo!")
                    print("FIN DEL JUEGO. ¡GANASTE! 🎉")
                elif cuarta_eleccion_derecha == "la ignoras":
                    print("\nIgnoras la cueva y sigues caminando sin rumbo. Te pierdes en el bosque.")
                    print("FIN DEL JUEGO. ¡PERDISTE! 💀")

            elif tercera_eleccion_seguir == "recto":
                print("\nSigues recto. El camino se vuelve más claro y te lleva a la salida del bosque.")
                print("FIN DEL JUEGO. ¡GANASTE! 🎉")

        elif segunda_eleccion_linterna == "buscar":
            print("\nDecides buscar entre los árboles lo que hizo el ruido. Te adentras en la maleza.")
            print("Encuentras un pequeño conejo asustado que huye. De repente, caes en un HUECO o puedes SALTAR a un lado. ¿Qué haces? 🐇")

            # --- Tercera decisión (Buscar): HUECO o SALTAR ---
            while True:
                tercera_eleccion_buscar = input().strip().lower()
                if tercera_eleccion_buscar in ["hueco", "saltar"]:
                    break
                else:
                    print("Opción no válida. Por favor, elige 'hueco' o 'saltar'.")

            if tercera_eleccion_buscar == "hueco":
                print("\nCaes en un hueco profundo y no puedes salir. Te quedas atrapado.")
                print("FIN DEL JUEGO. ¡PERDISTE! 💀")
            elif tercera_eleccion_buscar == "saltar":
                print("\nSaltas a un lado justo a tiempo. Evitas el hueco y encuentras un atajo que te saca del bosque.")
                print("FIN DEL JUEGO. ¡GANASTE! 🎉")

# Para iniciar el juego
jugar_juego()
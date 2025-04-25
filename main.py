from gramar_handler import tokenizar_produccion, clasificar_tokens, generar_gramatica, no_terminales, gramatica
from F_F_computer import calcular_first, calcular_follow

def main():
    print("Ingrese las producciones de la gramática (una por línea). Escriba 'fin' para terminar:")

    producciones = []

    while True:
        entrada = input()
        if entrada.lower() == 'fin':
            break
        producciones.append(entrada)
        # Tokenizar y clasificar la producción
        tokens = tokenizar_produccion(entrada)
        clasificacion = clasificar_tokens(tokens)

        print(f"Producción: {entrada}")
        print("Clasificación:", clasificacion)
        print()

    generar_gramatica(producciones)

    print("Producciones ingresadas:")

    for nt, prod in gramatica.items():
      print(f"{nt} -> {prod}")
    print("-------------------")
    for prod in producciones:
        print(prod)
    print()
    print("No terminales identificados:", no_terminales)
    print()

    #Calculamos el FIRST para cada no terminal

    first_dict = {}

    for nt in gramatica.keys():
      calcular_first(nt, first_dict)

    print("Conjuntos FIRST:")

    for nt, first in first_dict.items():
      print(f"FIRST({nt}) = {first}")
    print()

    #iniciamos el dict para almacenar los conjuntos follow

    follow_dict = {}
    start_symbol = list(gramatica.keys())[0]

    for nt in gramatica.keys():
      calcular_follow(nt, follow_dict, start_symbol, first_dict)

    print("Conjuntos Follow")
    for nt, follow in follow_dict.items():
      print(f"FOLLOW({nt}) = {follow}")
    print()

if __name__ == "__main__":
    main()
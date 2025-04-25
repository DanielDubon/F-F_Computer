from gramar_handler import tokenizar_produccion, clasificar_tokens, generar_gramatica, no_terminales, gramatica

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

if __name__ == "__main__":
    main()
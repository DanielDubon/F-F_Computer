from gramar_handler import gramatica, no_terminales, terminales

def calcular_first(no_terminal, first_dict):
    if no_terminal in first_dict:
       return first_dict[no_terminal]

    first_set = set()
    producciones = gramatica.get(no_terminal, [])

    for produccion in producciones:
        for simbolo in produccion:
            if simbolo in terminales:
               first_set.add(simbolo)
               break
            elif simbolo in no_terminales:
               first_of_symbol = calcular_first(simbolo, first_dict)
               first_set.update(first_of_symbol)
               if 'e' not in first_of_symbol:
                  break
            else:
                break
    first_dict[no_terminal] = first_set
    return first_set

def calcular_follow(no_terminal, follow_dict, start_symbol, first_dict):
    

    
    #print("ENTRANDO A CALCULAR FOLLOW del no terminal", no_terminal)
    #print("follow_dict", follow_dict)
    #print("start_symbol", start_symbol)
    #print("first_dict", first_dict)
    
      
    if no_terminal in follow_dict:
      #print("El terminal ya estaba en el dict")
      return follow_dict[no_terminal] # regresamos el resultado ya calculado

    follow_set = set()

    #Regla 1 si es el simbolo inicial agregamos el $
    if no_terminal == start_symbol:
       #print(f"Se cumplio la primera regla agregamos $ (no terminal {no_terminal} y start_symbol {start_symbol})")
       #print()
       follow_set.add('$')


    #Revisamos todas las producciones para encontrar A

    for B, producciones in gramatica.items():
        for produccion in producciones:
            for i, simbolo in enumerate(produccion):
                if simbolo == no_terminal:
                    #print(f"entramos al if del Simbolo = no terminal {simbolo} = {no_terminal} antes de la regla 2")
                    #print()
                    #Regla 2: si hay un simbolo despues de A
                    if i + 1 < len(produccion):
                        siguiente_simbolo = produccion[i + 1]
                        #print("Entramos al if de la regla 2 si hay un simbolo despues de A el siguiente simbolo es", siguiente_simbolo)
                        if siguiente_simbolo in terminales:
                            follow_set.add(siguiente_simbolo) #Agregamos el terminal
                        elif siguiente_simbolo in no_terminales:
                            #Agrega FIRST(del simbolo siguiente) excluyendo la e
                            first_of_next = calcular_first(siguiente_simbolo, first_dict)
                            follow_set.update(first_of_next - {'e'})
                            if 'e' in first_of_next:
                                #Regla 3: si First(el simbolo siguiente) contiene e
                                follow_set.update(calcular_follow(B, follow_dict, start_symbol, first_dict))

                    else:
                        # Regla 3: Si A es el último símbolo en la producción
                        if B != no_terminal:  # Avoid self-recursion for the same non-terminal
                            follow_set.update(calcular_follow(B, follow_dict, start_symbol, first_dict))

    follow_dict[no_terminal] = follow_set
    return follow_set

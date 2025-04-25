import re

# Definimos los terminales y no terminales
terminales = {'+', '*', '/', '(', ')', 'id', 'e'}
no_terminales = set()  # Usaremos un conjunto para almacenar no terminales
gramatica = {}

def tokenizar_produccion(produccion):

    patron = r'[A-Za-z]+\'?|[+\*/()]|id|e|->|\|'
    tokens = re.findall(patron, produccion)
    print("DEGBUG TOKENIZAR PRODUCCION:", tokens)

    return tokens

def clasificar_tokens(tokens):
    clasificacion = {}
    for token in tokens:
        if token in terminales:
            clasificacion[token] = 'terminal'
        elif token in no_terminales:
            clasificacion[token] = 'no_terminal'
        elif token == '->':
            clasificacion[token] = 'produccion'
        elif token == '|':
            clasificacion[token] = 'alternancia'
        elif token not in terminales and token not in no_terminales and token != '->' and token != '|':
            no_terminales.add(token)
            clasificacion[token] = 'no_terminal'

    return clasificacion

def generar_gramatica(producciones):
    for produccion in producciones:
        tokens = tokenizar_produccion(produccion)
        no_terminal = tokens[0]
        produccion = tokens[2:] # Los tokens después de '->' son la producción
        #manejamos la alternancia |

        if '|' in produccion:
            partes = ' '.join(produccion).split('|')  # Unir y dividir por '|'
            for parte in partes:
                parte_tokens = parte.strip().split()
                gramatica.setdefault(no_terminal, []).append(parte_tokens)
        else:
            gramatica.setdefault(no_terminal, []).append(produccion)
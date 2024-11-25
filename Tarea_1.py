def imprimir_combinaciones_dados_custom(valores_maximos, nivel=0, combinacion_actual=[]):
    """
    Genera un árbol de combinaciones para 5 dados con valores máximos configurables.
    
    Args:
        valores_maximos: Lista de 5 números indicando el valor máximo para cada dado
        nivel: Nivel actual en el árbol (usado internamente para la recursión)
        combinacion_actual: Lista de valores seleccionados hasta ahora (usado internamente)
    """
    # Si ya tenemos 5 dados, imprimimos la combinación
    if nivel == 5:
        print("    " * (nivel - 1) + "→ " + " ".join(map(str, combinacion_actual)))
        return
    
    # Para cada valor posible del dado actual (1 hasta el máximo especificado)
    for valor in range(1, valores_maximos[nivel] + 1):
        # Añadimos el nuevo valor a la combinación actual
        nueva_combinacion = combinacion_actual + [valor]
        
        # Imprimimos el nodo actual
        if nivel > 0:
            print("    " * (nivel - 1) + "├── " + str(valor))
        else:
            print(str(valor))
            
        # Recursivamente generamos el resto del árbol
        imprimir_combinaciones_dados_custom(valores_maximos, nivel + 1, nueva_combinacion)

def calcular_tamano_espacio_muestral(valores_maximos):
    """
    Calcula el tamaño total del espacio muestral.
    
    Args:
        valores_maximos: Lista de 5 números indicando el valor máximo para cada dado
    
    Returns:
        int: Número total de combinaciones posibles
    """
    total = 1
    aux =1
    for max_valor in valores_maximos:
        if max_valor != 0:
            total *= max_valor
        
    return total

# Ejemplo de uso
valores_maximos = [3, 3, 3, 0, 0]  # Ejemplo con dados típicos de D&D
print(f"Configuración de dados: D{valores_maximos[0]}, D{valores_maximos[1]}, D{valores_maximos[2]}, D{valores_maximos[3]}, D{valores_maximos[4]}")
print(f"Tamaño del espacio muestral: {calcular_tamano_espacio_muestral(valores_maximos)} combinaciones posibles")
print("\nÁrbol de combinaciones:")
print("----------------------")
imprimir_combinaciones_dados_custom(valores_maximos)
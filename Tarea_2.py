def generar_triangulo_pascal(n):
    """
    Genera el triángulo de Pascal hasta el exponente n.
    
    Args:
        n: Número de filas a generar (empezando desde 0)
    
    Returns:
        Lista de listas donde cada sublista representa una fila del triángulo
    """
    # Inicializamos el triángulo
    triangulo = []
    
    for i in range(n + 1):
        # Cada fila empieza y termina con 1
        fila = [1]
        
        # Calculamos los valores intermedios basados en la fila anterior
        if triangulo:
            fila_anterior = triangulo[-1]
            for j in range(len(fila_anterior) - 1):
                fila.append(fila_anterior[j] + fila_anterior[j + 1])
            fila.append(1)
            
        triangulo.append(fila)
    
    return triangulo

def imprimir_triangulo_pascal(triangulo):
    """
    Imprime el triángulo de Pascal de forma centrada y formateada.
    
    Args:
        triangulo: Lista de listas representando el triángulo de Pascal
    """
    # Encontrar el número más grande para determinar el ancho de cada número
    max_numero = max(max(fila) for fila in triangulo)
    ancho_numero = len(str(max_numero))
    
    # Encontrar el ancho de la última fila para centrar todo el triángulo
    ancho_total = len(triangulo[-1]) * (ancho_numero + 1) - 1
    
    # Imprimir cada fila centrada
    print(f"\nTriángulo de Pascal hasta n = {len(triangulo)-1}:")
    print("-" * (ancho_total + 4))  # Línea decorativa
    
    for i, fila in enumerate(triangulo):
        # Convertir números a strings con ancho fijo
        numeros = [str(num).center(ancho_numero) for num in fila]
        # Unir números con espacios y centrar la fila completa
        fila_str = " ".join(numeros)
        # Centrar la fila en el ancho total
        print(fila_str.center(ancho_total))
        
    print("-" * (ancho_total + 4))  # Línea decorativa
    

# Ejemplo de uso
while True:
    try:
        n = int(input("Ingrese el exponente para el triángulo de Pascal (0-20): "))
        if n < 0:
            print("Por favor ingrese un número no negativo.")
        elif n > 20:
            print("Por favor ingrese un número menor o igual a 20 para mantener una visualización clara.")
        else:
            triangulo = generar_triangulo_pascal(n)
            imprimir_triangulo_pascal(triangulo)
            break
    except ValueError:
        print("Por favor ingrese un número válido.")
def burbuja (numeros):
    """
    Ordena una lista de números utilizando el algoritmo de ordenamiento burbuja compara pares de elementos 
    juntos e intercambia sus posiciones si están en el orden incorrecto. Este proceso se repite hasta que 
    la lista se encuentra ordenada.
    Parámetros
    ----------
    numeros: list 
    Lista de números que se desea ordenar
    Retorna
    -------
    None
    La función no devuelve ningún valor, pero modifica la lista original.
    Ejemplo
    -------
    >>> burbuja([5, 2, 9, 1])
    [1, 2, 5, 9]
    """
    for i in range(0,len(numeros) - 1):
        for j in range(0,len(numeros) - i):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
    
# -----PROGRAMA PRINCIPAL-----
# Lista de números que queremos ordenar
numeros = [34, 12, 5, 66, 1, 89, 23]
print(numeros)
burbuja(numeros)
print(numeros)



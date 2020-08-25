def insertion_sort(lista): 
    n = len(lista)
    for i in range(1, n): 
        chave = lista[i]
        j = i - 1 
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1 
        lista[j + 1] = chave

def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        menor = j
        for i in range(j + 1, n):
            if lista[i] < lista[menor]:
                menor = i
        if lista[j] > lista[menor]:
            aux = lista[j] 
            lista[j] = lista[menor]
            lista[menor] = aux  


import random 
from sorting import insertion_sort, selection_sort

lista = random.sample(range(1,100), 30) 

if __name__ == "__main__":
    print("Antes do selection sort")
    print(lista)
    selection_sort(lista)
    print("Depois do selection sort")
    print(lista)

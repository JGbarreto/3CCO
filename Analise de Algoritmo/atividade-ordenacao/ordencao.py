from memory_profiler import memory_usage
import numpy as np
import argparse
import math
import time




def partition(arr, low, high):
    # Pega o último elemento como pivô
    pivot = arr[high]
    
    # Índice do menor elemento
    i = low - 1
    
    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        if arr[j] <= pivot:
            # Incrementa o índice do menor elemento
            i += 1
            # Troca arr[i] com arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Troca arr[i+1] com arr[high] (o pivô)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    global count_quick
    
    if low < high:
        # Encontra o índice do pivô
        pi = partition(arr, low, high)
        
        # Divide e conquista
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
    
    count_quick=count_quick + 1 

# Exemplo de uso:




def bubble_sort(arr):
    n = len(arr)
    global count_bubble
    # Percorre todos os elementos do array
    for i in range(n):
        
        # Últimos i elementos já estão no lugar certo, então não precisamos mais verificar eles
        for j in range(0, n-i-1):
            count_bubble+=1
            
            # Percorre o array de 0 a n-i-1
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
    return arr

# Exemplo de uso:


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("num", type=int)
    args= parser.parse_args()
    arr = np.round(np.random.rand(args.num) * 10, 1)
    arr2=arr.copy()
    count_bubble = 0
    count_quick = 0
    
    
    print("Bubble sort")
    n = len(arr)
    print("Tamanho do array:", n)
    print(f"Complexidade estimada: {n**2} iterações")
    inicio = time.time()
    bubble_sort(arr)
    fim = time.time() 
    tempo_processamento = fim - inicio
    memoria  = memory_usage()
    
    
    print(f"Uso máximo de memória: {memoria} MiB")
    print(f"Tempo de processamento: {tempo_processamento:.2f} segundos")
    print(f"Quantidade de ciclos: {count_bubble} iterações")
    

    time.sleep(5)
    print("Quick sort")
    n = len(arr2)
    print("Tamanho do array:", n)
    print(f"Complexidade estimada: {n * math.log10(n)} iterações")

    inicio2 = time.time() 
    quick_sort(arr2, 0, n-1)
    fim2 = time.time()
    tempo_processamento2 = fim2 - inicio2
    memoria = memory_usage()
    
    
    print(f"Uso máximo de memória: {memoria} MiB")
    print(f"Tempo de processamento: {tempo_processamento2:.2f} segundos")
    print(f"Quantidade de ciclos: {count_quick} iterações")
    


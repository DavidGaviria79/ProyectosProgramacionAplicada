def merge(arr, l, m, r):
    n1 = m - l + 1   # tamaño del subarreglo izquierdo
    n2 = r - m       # tamaño del subarreglo derecho

    # arreglos temporales
    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    i = 0    # índice inicial de L
    j = 0    # índice inicial de R
    k = l    # índice inicial de arr

    # mezclar L[] y R[]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # copiar los elementos restantes de L[]
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copiar los elementos restantes de R[]
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)       # ordenar mitad izquierda
        mergeSort(arr, m + 1, r)   # ordenar mitad derecha
        merge(arr, l, m, r)        # mezclar


# Ejemplo de uso
def main():
    arr = [10, 7, 8, 9, 1, 5]
    mergeSort(arr, 0, len(arr) - 1)

    print("Arreglo ordenado:")
    print(arr)


if __name__ == "__main__":
    main()

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high):
    pivot = arr[high]  # elegimos el último elemento como pivote
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1  # nueva posición del pivote


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)   # izquierda
        quickSort(arr, pi + 1, high)  # derecha


def printArray(arr):
    print(*arr)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    printArray(arr)

    quickSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    printArray(arr)


if __name__ == "__main__":
    main()

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # mover los elementos mayores que key hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insertar key en el hueco correcto
        arr[j + 1] = key


def print_array(arr):
    for x in arr:
        print(x, end=" ")
    print()


def main():
    arr = [5, 2, 4, 6, 1]

    print("Arreglo original:")
    print_array(arr)

    insertion_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)


if __name__ == "__main__":
    main()

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i  # asumimos que el menor está en i

        # buscar el menor en el resto del arreglo
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # si encontramos un menor, intercambiamos
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def print_array(arr):
    for x in arr:
        print(x, end=" ")
    print()


def main():
    arr = [5, 3, 6, 1, 4]
    print("Arreglo original:")
    print_array(arr)

    selection_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)


if __name__ == "__main__":
    main()

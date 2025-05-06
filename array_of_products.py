def array_of_products(arr: list[int]) -> list[int]:
    n = len(arr)
    left_products = [1] * n
    right_products = [1] * n
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * arr[i - 1]
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * arr[i + 1]
    return [left_products[i] * right_products[i] for i in range(n)]
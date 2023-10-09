def max_sequence(arr):
    max_sekarang = max_sejauh_ini = arr[0]

    for num in arr[1:]:
        max_sekarang = max(num, max_sekarang + num)
        max_sejauh_ini = max(max_sejauh_ini, max_sekarang)

    return max_sejauh_ini

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12

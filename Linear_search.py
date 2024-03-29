def search(v_list, n):
    # i = 0
    # while i < len(v_list):
    for i in range(0, len(v_list) + 1):
        if v_list[i] == n:
            return i + 1
        # i += 1
    return False


if __name__ == '__main__':
    my_list = [5, 8, 4, 6, 9, 2]

    pos = search(my_list, 9)

    if pos:
        print(f'Found at {pos}')
    else:
        print('Not found')

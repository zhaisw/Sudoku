import numpy as np


def possible_check(s, x, y):
    """
    Check possible values in a 9*9 Sudoku matrix
    :param s: Sudoku matrix
    :param x: x index
    :param y: y index
    :return: a list of possible values
    """
    result = np.array(range(1, 10))
    # horizontal check
    result = np.setdiff1d(result, s[x, :])
    # vertical check
    result = np.setdiff1d(result, s[:, y])
    # local region check 3*3 region
    region_idx = x // 3 + 1
    region_idy = y // 3 + 1
    local_s = s[(region_idx-1)*3:region_idx*3, (region_idy-1)*3:region_idy*3]
    result = np.setdiff1d(result, local_s[local_s > 0])
    return result


def refresh_possibles(s):
    possible_container = dict()
    for i in range(m):
        for j in range(n):
            if s[i, j] == 0:
                possibles = possible_check(s, i, j)
                # a position has no possible values
                if not np.any(possibles):
                    return None
                possible_container[(i, j)] = possibles
    return possible_container


def get_least(c):
    key = None
    tmp = 9
    for k in c:
        if len(c[k]) < tmp:
            key = k
            tmp = len(c[k])
    return key


def solve_sudoku(s):
    while True:
        tmp = s.copy()
        while True:
            possible_container = refresh_possibles(tmp)
            if not possible_container:
                break
            least_key = get_least(possible_container)
            val = np.random.choice(possible_container[least_key])
            tmp[least_key[0], least_key[1]] = val

        if np.all(tmp > 0):
            break

    return tmp


if __name__ == '__main__':
    sudoku = np.array([[0, 0, 0, 0, 7, 0, 0, 0, 0],
                       [0, 3, 2, 0, 0, 0, 7, 9, 0],
                       [0, 7, 0, 9, 5, 8, 0, 3, 0],
                       [0, 0, 7, 1, 0, 3, 5, 0, 0],
                       [6, 0, 1, 0, 0, 0, 4, 0, 3],
                       [0, 0, 5, 8, 0, 4, 1, 0, 0],
                       [0, 1, 0, 2, 4, 5, 0, 8, 0],
                       [0, 5, 9, 0, 0, 0, 3, 4, 0],
                       [0, 0, 0, 0, 3, 0, 0, 0, 0]])

    # get shape of Sudoku matrix
    m, n = sudoku.shape
    solved = solve_sudoku(sudoku)
    print(solved)

def rotate_clockwise(matrix):
    new_matrix = []
    for l in zip(*matrix):
        new_matrix.append(''.join(l[::-1]))
    return new_matrix
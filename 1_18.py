def page_rank():
    def calc_rank(pos, matrix, matrix_ranks):
        const_d = 0.85
        rank = (1 - const_d)
        column = [item[pos] for item in matrix]
        for i, item in enumerate(column):
            rank += const_d * item * (matrix_ranks[i] / sum(matrix[i]))

        return rank

    matrix = [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]
    matrix_ranks = [0.25] * len(matrix)
    epochs = 12
    for _ in range(epochs):
        for i in range(len(matrix)):
            matrix_ranks[i] = calc_rank(i, matrix, matrix_ranks)
        print(matrix_ranks)


page_rank()

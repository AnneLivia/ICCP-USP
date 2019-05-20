def dimensoes(matrix):
    lines = len(matrix)
    col = len(matrix[0])
    print(str(lines) + "x" + str(col))
def _main():
    minha_matriz = [[1, 2, 3], [4, 5, 6]]
    dimensoes(minha_matriz)

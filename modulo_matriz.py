def cria_matriz(num_lin, num_col, valor):
    mat = []
    for i in range(num_lin):
        linha = []
        for j in range(num_col):
            linha.append(valor)
        mat.append(linha)
    return mat

def soma_matriz(A, B):
    num_lin = len(A)
    num_col = len(A[0])
    mat = cria_matriz(num_lin, num_col, 0)
    for i in range(num_lin):
        for j in range(num_col):
            mat[i][j] = A[i][j] + B[i][j]
    return mat

def multi_matriz(A,B):
    num_linA, num_linB = len(A), len(B)
    num_colA, num_colB = len(A[0]), len(B[0])

    assert num_colA == num_linB
    mat = cria_matriz(num_linA, num_colB, 0)
    for i in range(num_linA):
        for j in range(num_colB):
            for k in range(num_colA):
                mat[i][j]+=(A[i][k] * B[k][j])
    return mat

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B =  [[1,2],[3,4],[5,6]]
    print(multi_matriz(A,B))
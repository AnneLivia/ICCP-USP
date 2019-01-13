def imprime_matriz(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j != 0:
                print(end=" ")
            print(str(matrix[i][j]), end="")
        print()
                

def soma_matrizes(m1,m2):
    dim1= [len(m1), len(m1[0])]
    dim2 = [len(m2), len(m2[0])]
    if(dim1[0] == dim2[0] and dim1[1] == dim2[1]):
           matrix = [] 
           for i in range(dim1[0]):
               linha = []
               for j in range(dim1[1]):
                   linha.append(m1[i][j] + m2[i][j])
               matrix.append(linha)
           return matrix
    else:
            return False
def main():
    m1 = [[1], [2], [3]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    return soma_matrizes(m1,m2)

#coding utf-8
def spiralOrder(matrix) :
    if len(matrix) == 0:
        return matrix
    if len(matrix) <= 1:
        return matrix[0]
    if len(matrix[0]) == 0:
        return []
    if len(matrix[0]) == 1:
        return [i[0] for i in matrix]
    ret = matrix[0]
    temp = []
    for i in range(1,len(matrix)-1):
        ret += [matrix[i][-1]]
        temp =  [matrix[i][0]] +temp
    ret += matrix[-1][::-1]
    ret += temp
    new_matrix =[ i[1:-1] for i in matrix[1:-1]]
    print(ret,new_matrix)


    return ret + spiralOrder(new_matrix)
def main():
    i = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    i = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    i = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    #i = [[1,2],[3,4]]
    print(spiralOrder((i)))


if __name__ == '__main__':
    main()
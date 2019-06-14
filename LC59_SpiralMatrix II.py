#coding utf-8
def generateMatrix( n ) :
    ret =[[0 for j in range(n)] for i in range(n)]
    m = 1
    N = n
    step =0
    row , col = 0 , 0
    while n >1:
        print( n,row ,col)
        ret[row][col] = m
        m +=1
        if step == 0:
            col += 1
            if col == (N + n )/2-1:
                step +=1
        elif step == 1:
            row += 1
            if row == (N + n )/2-1:
                step +=1
        elif step == 2:
            col -= 1
            if col == (N - n) //2 :
                step +=1
        elif step == 3:
            if  row == ( N - n )//2 +1:
                step =0
                n -= 2
                col +=1
            else:
                row -= 1
    if (N %2) :
        ret[N//2][N//2] =N*N
    return ret


def main():
    n =3
    print(generateMatrix(n))


if __name__ == '__main__':
    main()
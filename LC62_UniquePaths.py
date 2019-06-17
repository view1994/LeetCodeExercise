#coding utf-8

# 思路一：
#递归
#时间复杂度较高
def uniquePaths1(m: int, n: int) -> int:
    if (m == n):
        return 2 * uniquePaths(m - 1, n)
    elif (m > n):
        t = m
        m = n
        n = t
    if (m <=0) | (n<=0):
        return 0
    if (m ==1) |(n ==1):
        return 1
    if (m==2) :
        return n
    elif( n ==2):
        return m
    elif (m == 3):
        return n*(n+1)//2
    else:
        return uniquePaths(m-2 , n) + uniquePaths(m, n-2) + 2* uniquePaths(m-1,n-1)
        #return  uniquePaths(m-1 , n) + uniquePaths(m, n-1)
#思路二：
#将到达每个格子的路径数存在二维数组中，每个格子的值等于它上边格子和左边格子的和
#m x n 的数组中做一遍求和运算即可求出第mxn个格子的值
def uniquePaths(m: int, n: int) -> int:
    if (m > n):
        t = m
        m = n
        n = t
    #m<=n
    if (m <=0) | (n<=0):
        return 0
    if (m ==1) |(n ==1):
        return 1
    if (m==2) :
        return n
    elif( n ==2):
        return m
    elif (m == 3):
        return n*(n+1)//2
    array =[[0 for i in range(n)] for j in range(m)]
    #array[0] = [1 for i in range(n)]
    for i in range(1,n):
        array[0][i] = 1
        array[1][i] = i+1
        array[2][i] = (i+1)*(i+2)//2
    for j in range(1,m):
        array[j][0] = 1
        array[j][1] = j+ 1
        array[j][2] = array[2][j]
    for i in range(3,m):
        for j in range(3,n):
            array[i][j] = array[i-1][j]+array[i][j-1]
    return  array[-1][-1]
def main():
    m = 51
    n = 9
    print(uniquePaths(m,n))

if __name__ == '__main__':
    main()
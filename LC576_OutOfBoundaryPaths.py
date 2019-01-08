#coding utf-8
import time
def go1step(m, n, i, j,direction):
    if direction==1:
        return 1 if i==0 else 0
    elif direction==2:
        return 1 if i==m-1 else 0
    elif direction==3:
        return 1 if j == 0 else 0
    elif direction==4:
        return 1 if j == n-1 else 0
def go2step(m, n, i, j, N,start_step):
    x=0
    start_step+=1
    if start_step > N:
        return 0
    #----up
    x+=1 if go1step(m, n, i, j,1)==1 else go2step(m,n,i-1,j,N,start_step)
    #----down
    x += 1 if go1step(m, n, i, j,2)==1 else go2step(m,n,i+1,j,N,start_step)
    #----left
    x+=1 if go1step(m, n, i, j, 3)==1 else go2step(m,n,i,j-1,N,start_step)
    #----right
    x+=1 if go1step(m, n, i, j, 4)==1 else go2step(m,n,i,j+1,N,start_step)
    return x

def findPaths(self, m, n, N, i, j):
    """
    :type m: int
    :type n: int
    :type N: int
    :type i: int
    :type j: int
    :rtype: int
    """
    return go2step(m, n, i, j, N, 0)


# other solution ==========================================
def go1step1(m, n, i, j, N,start_step):
    x=0
    start_step+=1
    if start_step > N:
        return 0
    #----up
    x+=1 if i==0 else go1step1(m,n,i-1,j,N,start_step)
    #----down
    x += 1 if i==(m-1) else go1step1(m,n,i+1,j,N,start_step)
    #----left
    x+=1 if j==0 else go1step1(m,n,i,j-1,N,start_step)
    #----right
    x+=1 if j==(n-1) else go1step1(m,n,i,j+1,N,start_step)
    return x
def  GoOutAtStepN(m, n, i, j, N):
    return go1step1(m, n, i, j, N,0)-go1step1(m, n, i, j, N-1,0)
def main():
    t=time.time()
    print(go1step1(8, 3, 1, 1, 8, 0))
    #print(go1step(1, 3, 1, 1, 2, 0))
    print(time.time()-t)
if __name__ == '__main__':
    main()

'''#coding utf-8
import time
def out_paths_in1step(m,n,i,j):
    x=0
    if (i>=m )|(j>=n ):
        return 0
    x+=1 if i==0 else 0
    x+=1if i==(m-1) else 0
    x+=1 if j==0 else 0
    x+=1 if j==(n-1) else 0
    print('1step-> m={},n={},i={},j={}\tx={}'.format(m,n,i,j,x))
    return x
def go2step_out(m, n, i, j, N,start_step):
    x=0
    start_step += 1
    if start_step ==N:
     #   return 0
    #elif start_step==N-1:
        return out_paths_in1step(m, n, i, j)

    #----up
    x+=1 if i==0 else go2step_out(m,n,i-1,j,N,start_step)
    #----down
    x += 1 if i==(m-1) else go2step_out(m,n,i+1,j,N,start_step)
    #----left
    x+=1 if j==0 else go2step_out(m,n,i,j-1,N,start_step)
    #----right
    x+=1 if j==(n-1) else go2step_out(m,n,i,j+1,N,start_step)
    return x
def main():
    t=time.time()
    #print(go2step_out(10,10,5,5,11,0))
    print(go2step_out(1, 3, 1, 1, 2, 0))
    print(time.time()-t,'s')
if __name__ == '__main__':
    main()
    
'''
'''
def go1step(m, n, i, j,direction):
    if direction==1:
        return 1 if i==0 else 0
    elif direction==2:
        return 1 if i==m-1 else 0
    elif direction==3:
        return 1 if j == 0 else 0
    elif direction==4:
        return 1 if j == n-1 else 0
def go2step_out(m, n, i, j, N,start_step):
    x=0
    start_step+=1
    if start_step > N:
        return 0
    #----up
    x+=1 if i==0 else go2step_out(m,n,i-1,j,N,start_step)
    #----down
    x += 1 if i==(m-1) else go2step_out(m,n,i+1,j,N,start_step)
    #----left
    x+=1 if j==0 else go2step_out(m,n,i,j-1,N,start_step)
    #----right
    x+=1 if j==(n-1) else go2step_out(m,n,i,j+1,N,start_step)
    return x

'''

'''

def go2step_out(m, n, i, j, N,start_step):
    x=0
    start_step+=1
    if start_step > N:
        return 0
    #----up
    x+=1 if go1step(m, n, i, j,1)==1 else go2step_out(m,n,i-1,j,N,start_step)
    #----down
    x += 1 if go1step(m, n, i, j,2)==1 else go2step_out(m,n,i+1,j,N,start_step)
    #----left
    x+=1 if go1step(m, n, i, j, 3)==1 else go2step_out(m,n,i,j-1,N,start_step)
    #----right
    x+=1 if go1step(m, n, i, j, 4)==1 else go2step_out(m,n,i,j+1,N,start_step)
    return x
t=time.time()
print(go2step_out(10,10,5,5,10,0))
print(time.time()-t)

'''

'''
test_sample=[[2, 2, 0, 0, 1, 2],
             [2, 2, 0, 0, 2, 6],
             [2, 2, 0, 0, 3, 14],
             [1, 3, 0, 1, 1, 2],
             [1, 3, 0, 1, 2, 8],
             [1, 3, 0, 1, 3, 12],
             [3,3,1,1,1,0],
             [3,3,1,1,2,4],
             [3,3,1,1,3,20],
             [3,3,0,1,1,1],
             [3,3,0,1,2,5]
             ]

def out1step(param):
    x=0
    [m, n, i, j, N, key] = param
    x+=1 if i==0 else 0
    x+=1 if i==m-1 else 0
    x+=1 if j==0 else 0
    x+=1 if j==n-1 else 0
    return x

def way2out(param):
    [m,n,i,j,N,key]=param
    if N==1:
        x=out1step(param)
        return x
        #print('m={},n={},i={},j={},x={},key={}'.format(m,n,i,j,x,key))
    elif N==2:
        x=out1step([m,n,i,j,N-1,key])
        #print('m={},n={},i={},j={},x(N-1)={},key={}'.format(m, n, i, j, x, key))


for i in test_sample:
    x=go2step_out(i,0)
    #print('{}\t{}'.format(x,i[-1]))

'''
#coding utf-8
def reverse(x):
    if  ( x > 0 ) & ( x <= pow( 2 , 31 ) - 1 ):
        t=str(x)
        y=int(t[::-1])
        if  y > pow( 2 , 31 ) - 1 :
            return 0
        else:
            return y
    elif ( x < 0 ) & ( x >= - pow( 2, 31)):
        t = str( x )
        y = - int( t[ ::-1 ] [:-1])
        if y < - pow( 2, 31):
            return 0
        else:
            return y
    else:
        return 0
def main():
    n=1534236469
    print(reverse(n))
if __name__ == '__main__':
    main()
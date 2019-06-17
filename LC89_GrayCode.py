#coding utf-8
'''
关键是搞清楚格雷编码的生成过程, G(i) = i ^ (i/2);
        如 n = 3:
        G(0) = 000,
        G(1) = 1 ^ 0 = 001 ^ 000 = 001
        G(2) = 2 ^ 1 = 010 ^ 001 = 011
        G(3) = 3 ^ 1 = 011 ^ 001 = 010
        G(4) = 4 ^ 2 = 100 ^ 010 = 110
        G(5) = 5 ^ 2 = 101 ^ 010 = 111
        G(6) = 6 ^ 3 = 110 ^ 011 = 101
        G(7) = 7 ^ 3 = 111 ^ 011 = 100
'''
def grayCode(n: int) :
    b ='0b'+ '1'*n
    x = eval(b)
    print(b,x)
    ret =[]
def main():
    print(grayCode(3))


if __name__ == '__main__':
    main()
#coding utf-8
def multiply(num1: str, num2: str) -> str:
    # 脑残解法
    #return str(int( num1)*int( num2))
    if (num1 == '0') | (num2 == '0'):
        return '0'
    ret = ''
    for i in range(len(num1)):
        for j in range(len(num2)):
            #print(ret)
            n1 = ord(num1[-i-1]) - ord('0')
            n2 = ord(num2[-j-1]) - ord('0')
            m = n1 * n2         #max_m = 81
            n = m % 10
            m = m // 10
            #t = chr(ord('0') + m) + chr(ord('0') + n) + '0'*(i+j)
            #print( i,j,n1 ,n2 , t)
            if len(ret)<(i+j):
                ret = '0'*(i+j-len(ret)) +ret
            if  len(ret) == (i+j):
                ret = chr(m+ord('0'))+chr(n+ord('0'))+ret
                continue
            if len(ret) >= (i+j+1):     #+n
                t = ord(ret[-(i+j+1)]) - ord('0')+n
                if t >=10:
                    m +=1
                ret = ret[:-(i+j+1)] + chr(t%10+ord('0')) + ret[-(i+j):]
            if len(ret) == (i+j+1):
                ret = chr(m+ord('0')) + ret
                continue
            else:  #if len(ret) >= (i + j + 2)    # +m          max_m=9
                t = ord(ret[-(i + j + 2)]) + m -ord('0')
                if t>=10:
                    if len(ret) > (i + j + 2):
                        ret = ret[:-(i+j+3)] + chr(ord(ret[-(i+j+3)])+1) +ret[-(i+j+2):]
                    else:
                        ret = '1'+ret
                ret = ret[:-(i+j+2)] + chr(t%10+ord('0')) + ret[-(i+j+1):]
    if ret[0] == '0':
        ret = ret[1:]
    return ret
def main():
    num1 = "123"
    num2 = "45"
    print(multiply(num1,num2))


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
#

def intToRoman(num):
    """
    :type num: int
    :rtype: str

    字符字           数值
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    """
    str = ''
    i = num % 10
    x = num % 100 // 10
    c = num % 1000 // 100
    m = num //1000
    #1000
    for j in range(m):
        str += 'M'
    #100
    if c == 9:
        str += 'CM'
    elif 5 <= c < 9 :
        str += 'D'
        for j in range(c-5):
            str += 'C'
    elif c ==4:
        str += 'CD'
    elif 0 < c < 4 :
        for j in range(c):
            str += 'C'
    #10
    if x == 9:
        str += 'XC'
    elif 5 <= x < 9 :
        str += 'L'
        for j in range(x-5):
            str += 'X'
    elif x == 4:
        str += 'XL'
    elif 0 < x < 4 :
        for j in range(x):
            str += 'X'
    #1
    if i == 9:
        str += 'IX'
    elif 5 <= i < 9 :
        str += 'V'
        for j in range(i-5):
            str += 'I'
    elif i == 4:
        str += 'IV'
    elif 0 <= i < 4:
        for j in range(i):
            str += 'I'
    return str

def main():
    n=1234
    print(intToRoman(n))


if __name__ == '__main__':
    main()
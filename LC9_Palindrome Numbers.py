#coding utf-8
def isPalindrome(x):
    s=str(x)
    for i in range(len(s)//2):
        if s[i] != s[ -1-i ]:
            return False
    return True
def isPalindrome1(x):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False
def isPalindrome2(x):
    if x < 0 :
        return False
    else:
        l=[]
        while x:
            l.append(x%10)
            x=x//10
        if l==l[::-1]:
            return True
        else:
            return False
def main():
    n=1-1
    print(isPalindrome(n))

if __name__ == '__main__':
    main()
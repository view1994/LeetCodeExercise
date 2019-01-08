#coding utf-8
#Shortest Palindrome
#给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
def shortestPalindrome( s):
    """
    :type s: str
    :rtype: str
    """
    for lens in range(len(s),0,-1):
        i = lens // 2
        if lens%2:
            if s[ : i ] == s[2*i :i :-1]:
                return s[-1:2*i :-1]+s
        else:
            if s[0:(i)]==s[i:(2*i)][::-1]:
                return s[2*i:][::-1]+s
    return s

def main():
    s=''
    print(shortestPalindrome(s))


if __name__ == '__main__':
    main()
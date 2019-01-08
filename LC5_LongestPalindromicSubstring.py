#coding utf-8

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''
from functools import reduce
def find_substring(str):
    sub=''
    L = len(str)
    for i in range(L):
        l = len(sub)
        if l>L-i:
            return sub
        for j in range(i+2,L+1):
            s=str[i:j]
            if s==s[::-1]:
                if j-i > l:
                    sub=s
    if str == '':
        sub = ''
    elif sub=='':
        sub=str[0]
    return sub

def main():
    str="dvdf"
    print(find_substring(str),'',sep='\n')
if __name__ == '__main__':
    main()


def find_substring1(s):
    substr=''
    substrs=[]
    for i in range(len(s)):
        if s[i] not in substr:
            substr+=s[i]
        else:
            substrs.append(substr)
            substr=s[s[:i].rindex(s[i])+1:i+1]
    substrs.append(substr)
    for i in substrs:
        if len(i)>len(substr):
            substr=i
    return substr
# -*- coding: utf-8 -*-
#

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    s = ''
    flag =True
    if strs:
        for i in range(len(strs[0])):
            t = strs[0][i]
            for j in strs[1:]:
                if len(j)<=i:
                    return s
                elif j[i] != t:
                    return s
            else:
                s += t
    return s

def main():
    strs = ["flower","flo","flowet"]
    print(longestCommonPrefix(strs))



if __name__ == '__main__':
    main()
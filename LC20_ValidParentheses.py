# -*- coding: utf-8 -*-
#
#def can_match(a,b):
#    return  True if (a,b) in zip('([{', ')]}') else False

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    can_match=lambda a,b:True if (a,b) in zip('([{', ')]}') else False
    right=[]
    li=list(s)
    while li:
        i=li.pop()
        if i in ')]}':
            right.append(i)
            if not li:
                return False
        elif i in '([{':
            if not right:
                return False
            if not can_match(i,right.pop()):
                return False
    if not right:
        return True
    else:
        return False

def main():
    s='[]}'
    #can_match('}','{')
    print(isValid(s))


if __name__ == '__main__':
    main()
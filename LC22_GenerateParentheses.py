# -*- coding: utf-8 -*-
#
import copy
def left_minus_right(s):
    l=0
    r=0
    for i in s :
        if i =='(':
            l+=1
        elif i==')':
            r+=1
    return l-r
def generateParenthesis( n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        if n==1:
            return ['()']
        result = generateParenthesis(n-1)
        result_new=[]
        for s in result:
            len_s =len(s)
            s_save = copy.deepcopy(s)
            for i in range(len_s) :
                s = copy.deepcopy(s_save)
                s = s[:i] + '(' + s[i:]
                s_save1=copy.deepcopy(s)
                for j in range(i,len_s+1):
                    s=copy.deepcopy(s_save1)
                    #print('s=',s,'j=',j,'key=',left_minus_right(s[:j]))
                    if left_minus_right(s[:j])>=1:
                        s = s[:j] + ')' + s[j:]
                        if s not in result_new:
                            result_new.append(s)
                        #print(result_new)
        #result=result_new
        #print('return result_new of ',n,' is ',result_new)
        return result_new
def main():
    print(generateParenthesis(3))


if __name__ == '__main__':
    main()
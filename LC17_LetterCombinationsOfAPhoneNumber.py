#coding utf-8
import  copy,time
Map = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    result = ['']
    tem=[]
    for i in digits:
        tem.append(Map[i])
    if not tem:
        return []
    for i in tem:
        result_new = []
        for j in i :
            for k in result:
                s = k+j
                result_new.append(s)
        result=copy.deepcopy(result_new)
    return  result

def main():
    print(letterCombinations('23'))


if __name__ == '__main__':
    main()
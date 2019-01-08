#coding utf-8
#
def convert(s, numRows):
    l=[[] for i in range(numRows)]
    s=list(s)
    while len(s):
        for i in range(numRows):
            if len(s):
                l[i]+=s.pop(0)
            else:
                break
        for j in range(numRows-2,0,-1):
            if len(s):
                l[j]+=list(s.pop(0))
            else:
                break
    l=''.join([''.join(i) for i in l])
    return l
def main():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numRows = 4
    print(s)
    print( convert( s , numRows ) )
    print("PINALSIGYAHRPI")
if __name__ == '__main__':
    main()
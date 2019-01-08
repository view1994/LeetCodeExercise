#coding utf-8
import time
def atoi(str):
    l=str.strip().split()
    if len(l)==0:
        return 0
    elif l[0][0] in '0123456789+-':
        sub_str=l[0]
        if len(sub_str)==1:
            if sub_str in '+-':
                return 0
            else:
                return int(sub_str)
        else:
            for i in range(1,len(sub_str)):
                if sub_str[i] not in '0123456789':
                    break
            else:
                i+=1
            try:
                y=int( sub_str[:i])
            except:
                print('try int( "{}"[:{}])   except  ->0'.format(sub_str,i))
                return 0
            if y > pow(2,31)-1:
                return pow(2,31)-1
            elif  y < -pow(2,31):
                return -pow(2,31)
            else:
                return y
    else:
        return 0
def main():
    s='                     101234567890 -5646bbb  dfd  f56 rr655ff'
    t=time.time()
    print(atoi( s ))
    print(time.time()-t)
if __name__ == '__main__':
    main()
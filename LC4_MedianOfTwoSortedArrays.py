#coding utf-8
def find_median(num1,num2):
    m=len(num1)
    n=len(num2)
    if(m+n)%2:
        return sorted(num1+num2)[(m+n-1)//2]
    else:
        return (sorted(num1+num2)[(m+n)//2]+sorted(num1+num2)[(m+n)//2-1])/2

def main():
    num1=[1,2]
    num2=[3,4]
    print(find_median(num1,num2))
if __name__ == '__main__':
    main()
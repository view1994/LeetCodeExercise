#coding utf-8
def permute( nums):
    if len(nums) == 1 :
        return [nums]
    n = nums[0]
    ret  =[]
    t = permute(nums[1:])
    for j in t:
        for i in range(0,len(j)+1):
            ret .append( j[:i] + [n ]+ j[i:])
    return ret
def main():
    l = [1,2,3,4]
    print(permute(l))

if __name__ == '__main__':
    main()
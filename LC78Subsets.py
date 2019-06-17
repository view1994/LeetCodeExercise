#coding utf-8
def subsets(nums) :
    if len(nums) ==0:
        return [[]]
    elif len(nums)==1:
        return [[],nums]
    else:
        ret = []
        t = subsets(nums[1:])
        print(t)
        for i in t:
            ret.append(i)
            ret.append([nums[0]]+i)
        return ret
def main():
    nums = [1, 2, 3]
    print(subsets(nums))


if __name__ == '__main__':
    main()
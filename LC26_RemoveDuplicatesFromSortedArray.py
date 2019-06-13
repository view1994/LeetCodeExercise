#coding utf-8
def removeDuplicates( nums) -> int:
    if len(nums) <= 1:
        return  len(nums)
    i = 0
    j = 0
    while i < len( nums)-1:
        if(nums[i] == nums[i+1] ):
            i += 1
        else:
            j += 1
            i += 1
            nums[j] = nums[ i ]
    return j+1


def main():
    L = [0,0,1,1,1,2,2,3,3,4]
    #L = [1,1]
    x = removeDuplicates(L)
    print(x,L[:x])


if __name__ == '__main__':
    main()
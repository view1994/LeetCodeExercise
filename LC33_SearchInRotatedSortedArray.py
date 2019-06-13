#coding utf-8
from math import  log

#二分法查找的时间复杂度为O(log n)
#要求算法时间复杂度必须是 O(log n) 级别。
#说明本题可借助二分法解决
# 先二分法查找旋转点，排除旋转点后二分法查找目标
def binary_search(L, key):
    if len(L) ==0:
        return -1
    elif len(L) ==1:
        return 0 if L[0] ==key else -1
    low = 0
    high = len(L)-1
    med = high//2
    if L[low] == key:
        return low
    elif L[high] ==key:
        return high
    else:
        if L[med] < key:
            t = binary_search(L[med+1:],key)
            return t if t ==-1 else t+med+1
        elif L[med] > key:
            return  binary_search(L[:med],key)
        else:
            return med
def search(nums, target: int) -> int:
    Len = len(nums)
    if Len==0:
        return -1
    med = Len//2
    if (target<nums[0] )&( target > nums[-1]):
        return -1
    if nums[0] <nums[-1]:
        return binary_search(nums,target)
    if nums[med] > nums[0]:
        #rotate point 在后边
        if target==nums[med]:
            return med
        elif (target>=nums[0])&(target<nums[med]):
            return  binary_search(nums[:med],target)
        else :
            k = search(nums[med+1:],target)
            return  -1 if k==-1 else med +1 +k
    else:
        # rotate point 在前边
        if target==nums[med]:
            return med
        elif (target>nums[med])&(target<=nums[-1]):
            k = binary_search(nums[med+1:],target)
            return k if k==-1 else k + med +1
        else:
            return search(nums[:med],target)

def main():
    nums = [9,10,0, 1,3,4,5,6]
    target = 5
    print(search(nums,target))

if __name__ == '__main__':
    main()
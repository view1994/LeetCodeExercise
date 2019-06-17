#coding utf-8
#failed
def merge1(nums1 , m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    if n ==0:
        return
    if m ==0:
        nums1=nums2
    i = 0
    t = nums2.pop(0)
    n-=1
    while (m >0)&(n>0):
        if t<= nums1[i]:
            nums1.insert(i,t)
            t = nums2.pop(0)
            n -= 1
            #i+=1
            m+=1
            print( i , t,m ,n)
        m -= 1
        i+=1
    else:
        print(i, t, m, n, nums1, nums2)
        if m ==0:
            nums1.insert(i, t)
            i += 1
            nums1[i:] = nums2
        if n ==0:
            if t<=nums1[i]:
                nums1.insert(i,t)
            else:
                i+=1
                nums1.insert(i, t)
            nums1[:] = nums1[:i+m]

#执行用时 :52 ms, 在所有Python3提交中击败了91.83%的用户
#内存消耗 :13.1 MB, 在所有Python3提交中击败了86.01%的用户
#两层循环嵌套，nums2为外层循环，内层循环只跟着nums1的指针循环
# 因此时间复杂度是n，而不是n*m
def merge(nums1, m: int, nums2, n: int) -> None:
    i = 0
    L =m+n
    for t in nums2:
        while i<m:
            if t <= nums1[i]:
                nums1.insert(i,t)
                m+=1
                break
            i+=1
        else:
            nums1.insert(i,t)
            i += 1
    #print(nums1)
    nums1[:] =nums1[:L]
    return
def main():
    nums1 = [0]#[1, 2, 4,7, 0, 0, 0]
    m = 1
    nums2 =[1]# [2, 3, 6]
    n = 1
    merge(nums1,m,nums2,n)
    print(nums1)
if __name__ == '__main__':
    main()
#coding utf-8
import time
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result=[]
    nums.sort()
    if  len(nums)<4:
        return []
    elif target>nums[-1]+nums[-2]+nums[-3]+nums[-4]:
        return []
    elif target<nums[0]+nums[1]+nums[2]+nums[3]:
        return []
    le = len(nums)
    i = 0
    while (i < le - 3) :
        if (nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target):
            break
        j = le - 1
        while (j > i+2)  :
            if (nums[j]+nums[j-1]+nums[j-2]+nums[j-3] <target):
                break
            k = i + 1
            l = j -1
            target_kl = target - nums[i] - nums[j]
            while (k < l):
                if (nums[k] +nums[k+1] > target_kl):
                    break
                if (nums[l] + nums[l-1] < target_kl):
                    break
                target_kl = target - nums[i] - nums[j]
                if (target_kl == nums[k] + nums[l]):
                    result.append([nums[i],nums[k],nums[l],nums[j]])
                    while(nums[k]==nums[k+1])&(k<l-1):
                        k += 1
                    k += 1
                    while(nums[l]==nums[l-1])&(l>k+1):
                        l -= 1
                    l -= 1
                elif(target_kl > nums[k] + nums[l]):
                    k +=1
                elif(target_kl < nums[k] + nums[l]):
                    l -= 1
            while (nums[j-1] == nums[j])&(j>i+3):
                j -= 1
            j -= 1
        while((nums[i] == nums[i+1])&(i<le-4)):
            i += 1
        i += 1
    return result

def main():
    #222
    nums =[-474,-445,-442,-426,-410,-382,-369,-367,-356,-351,-339,-335,-335,-320,-318,-313,-276,-250,-227,-215,-209,-209,-200,-198,-189,-183,-154,-149,-138,-134,-121,-110,-97,-93,-86,-66,-61,-54,-33,-12,-9,2,6,13,30,59,82,86,88,111,132,159,162,193,204,220,225,229,231,275,314,327,332,386,400,440,452,457,485]
    target = 3456
    #225
    nums=[-495, -477, -464, -424, -411, -409, -363, -337, -328, -328, -325, -320, -310, -285, -278, -235, -208, -151, -149,
     -147, -144, -132, -115, -107, -101, -98, -83, -58, -58, -56, -51, -46, -45, -7, 0, 4, 4, 21, 51, 52, 57, 60, 104,
     109, 124, 141, 158, 205, 206, 241, 278, 278, 291, 314, 379, 416, 437, 447, 452, 496]
    target=-1371
    #239
    nums = [-492,-465,-454,-450,-416,-403,-384,-378,-377,-368,-360,-341,-325,-322,-315,-310,-309,-284,-275,-274,-271,-264,-255,-248,-245,-232,-222,-212,-211,-204,-184,-137,-133,-128,-120,-117,-109,-92,-88,-61,19,19,32,37,39,55,60,94,98,187,187,216,254,272,284,284,290,295,323,328,336,411,428,440]
    target=1154
    #260            time=0.796875
    nums=[-494,-474,-425,-424,-391,-371,-365,-351,-345,-304,-292,-289,-283,-256,-236,-236,-236,-226,-225,-223,-217,-185,-174,-163,-157,-148,-145,-130,-103,-84,-71,-67,-55,-16,-13,-11,1,19,28,28,43,48,49,53,78,79,91,99,115,122,132,154,176,180,185,185,206,207,272,274,316,321,327,327,346,380,386,391,400,404,424,432,440,463,465,466,475,486,492]
    target=-1211
    nums = [-5,5,4,-3,0,0,4,-2]
    target = 4
    nums = [0,0,0,0]
    target=0
    nums = [-1,-5,-5,-3,2,5,0,4]
    target =-7
    nums =[1,0,-1,0,-2,2]
    target=0
    t=time.time()
    res = fourSum(nums,target )
    print(res ,len(res))
    print(time.time()-t)

if __name__ == '__main__':
    main()
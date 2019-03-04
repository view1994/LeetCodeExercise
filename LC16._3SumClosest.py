#coding utf-8
import time, functools
def metric(func):
    functools.wraps(func)
    def wrapper(*arg, **kw):
        t_start = time.time()
        result = func(*arg, **kw)
        print('run %s spent %s s'%(func.__name__, time.time() - t_start ))
        return  result
    return wrapper
def threeSumClosest1( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
        return None
    elif len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
    else:
        nums.sort()
        print(nums, target)
        n = nums.pop(0)
        i = 0
        j = len(nums) - 1
        x = nums[i]
        y = nums[j]
        re_n = n + x + y
        re = re_n
        last = re_n - target
        d = last
        while len(nums) >= 2:
            while (i + 1 < j):
                #print("n={}\tx={}\ty={}\tre_n={}\tlast={}\td={}".format(n, x, y, re_n, last, d))
                if last > 0:
                    j -= 1
                    y = nums[j]
                    temp = n + x + y
                    this = temp - target
                    print("n={}\tx={}\ty={}\tre_n={}\tlast={}\td={}".format(n, x, y, re_n, last, d),end='')
                    print("this={}".format(this))

                    # print("this={},x={},y={}".format(this,x,y))
                    if this < 0:
                        if -this <= abs(d):
                            re_n = temp
                            d = this
                        last = this
                    else:
                        if this < d:
                            d = this
                        re_n = temp
                        last = this
                elif last < 0:
                    i += 1
                    x = nums[i]
                    temp = n + x + y
                    this = temp - target
                    print("n={}\tx={}\ty={}\tre_n={}\tlast={}\td={}".format(n, x, y, re_n, last, d), end='')
                    print("this={}".format(this,x,y))
                    if this > 0:
                        if this <= abs(d):
                            re_n = temp
                            d = this
                        last = this
                    else:
                        if this > d:
                            d = this
                        re_n = temp
                        last = this
                else:
                    return re_n
            else:
                # compare re_n with re
                print("==n={}\tre_n={}\tlast={}\td={}".format(n,re_n,last,d))
                if abs(d) < abs(re - target):
                    re = re_n
                    if abs(last) == 0:
                        return re
                n = nums.pop(0)
                i = 0
                j = len(nums) - 1
                x = nums[i]
                y = nums[j]
                re_n = n + x + y
                last = re_n - target
                if abs(re_n - target) < abs(d):
                    d = re_n - target
                    re = re_n
        else:
            print(re, "end")
            return re
@metric #time decoration
def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    print('target= {1}\nnums={0}'.format(nums, target))
    Result = None
    Diff = None     #Diff = Result - target
    if len(nums) < 3:
        return None
    elif len(nums) == 3:
        return nums[0] + nums[1] + nums[2]
    else:
        while (len(nums) >= 3):
            n = nums.pop(0)
            i = 0
            j = len(nums) - 1
            diff_n = None
            sum_n = None
            print('\n==>n = {}\tDiff = {}\tResult ={}'.format(n, Diff, Result))
            while ( i < j ):
                x = nums [i]
                y = nums [j]
                s = n + x + y
                diff = s - target
                print('\tx = {}, y = {},\tdiff_n= {},sum_n ={},\tdiff = {}, s={},'.format(x, y , diff_n, sum_n, diff, s),end='\t\t->')
                if diff == 0:
                    print('\nreturn  target\n')
                    return target
                elif diff_n == None:
                    diff_n ,sum_n = diff , s
                    if diff > 0:
                        j -= 1
                    else:
                        i += 1
                elif (diff >0)  :
                    if abs(diff) < abs(diff_n):
                        diff_n, sum_n = diff, s
                    j -= 1
                elif (diff < 0)  :
                    if abs(diff) < abs(diff_n):
                        diff_n, sum_n = diff, s
                    i += 1
                print('i ={}, j= {},diff_n ={},sum_n={}'.format(i,j,diff_n,sum_n))
            else:
                if Result == None:
                    Result, Diff = sum_n, diff_n
                elif abs(diff_n) < abs(Diff):
                    Result, Diff = sum_n , diff_n
        else:           #len(nums) == 3
            temp_r =  nums[0] + nums[1] +n
            if Result == None:
                Result= temp_r
            else:
                temp_d = temp_r - target
                if abs(temp_d) < abs(Diff):
                    Result , Diff = temp_r , temp_d
        return Result



def main():
    nums , target = [1,2,5,10,11],12
    nums ,target = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33],0
    nums, target = [4, 0, 5, -5, 3, 3, 0, -4, -5],-2

    #
    nums, target = [87, 6, -100, -19, 10, -8, -58, 56, 14, -1, -42, -45, -17, 10, 20, -4, 13, -17, 0, 11, -44, 65, 74, -48, 30, -91,
     13, -53, 76, -69, -19, -69, 16, 78, -56, 27, 41, 67, -79, -2, 30, -13, -60, 39, 95, 64, -12, 45, -52, 45, -44, 73,
     97, 100, -19, -16, -26, 58, -61, 53, 70, 1, -83, 11, -35, -7, 61, 30, 17, 98, 29, 52, 75, -73, -73, -23, -75, 91,
     3, -57, 91, 50, 42, 74, -7, 62, 17, -91, 55, 94, -21, -36, 73, 19, -61, -82, 73, 1, -10, -40, 11, 54, -81, 20, 40,
     -29, 96, 89, 57, 10, -16, -34, -56, 69, 76, 49, 76, 82, 80, 58, -47, 12, 17, 77, -75, -24, 11, -45, 60, 65, 55,
     -89, 49, -19, 4],-275  #-274
    #nums, target = [0, 2, 1, -3], 1#0
    nums, target = [-1, 2, 1, -4], 1  # 2
    nums, target = [1, 1, -1, -1, 3], -1#-1
    nums, target =[1, 2, 4, 8, 16, 32, 64, 128],82#82
    nums, target =[1,6,9,14,16,70],81#80
    print(threeSumClosest(nums, target))


if __name__ == '__main__':
    main()
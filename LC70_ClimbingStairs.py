#coding utf-8
#思路1：
#此问题直接计算较麻烦，可考虑递归
#递归思路：
#最后一步有两种可能，要么爬一步，要么爬两步
#爬一步的可能数跟爬前面的n-1步的可能数一样多
#爬两步的可能数跟爬前面的n-1步的可能数一样多
#所以结果把这两种情况加起来就可以了
#基例就是n=1和n=2的情况
def climbStairs1(n: int) -> int:
    if n == 1:
        return 1
    if n ==2:
        return 2
    else:
        return climbStairs(n-1)+climbStairs(n-2)
#思路2：
#直接递归的重复计算太多，实际本次计算n-1的情况和上次计算的n-2是同样的情况
#如果能记下上次计算的中间值并重复利用就好了
#本问题实际就是要算斐波那契数列
#数列+for循环 实现即可
#执行用时 :44 ms, 在所有Python3提交中击败了94.72%的用户
#内存消耗 :12.9 MB, 在所有Python3提交中击败了97.43%的用户
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n ==2:
        return 2
    else:
        array = [ 0,1, 2]
        for i in range(3,n+1):
            array.append( array[i-1]+array[i-2])
        return array[n]
def main():
    print(climbStairs(35))#8


if __name__ == '__main__':
    main()
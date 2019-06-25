# -*- coding: utf-8 -*-
#
#思路：动态规划
#重点是找出前一天和当天最大收益间的关系，构成递归结构
#也就是已知前i-1天的最大收益，如何求加上第i天的价格后的最大收益
#也就是假设最后一天卖出股票，则最大收益应该在前i-1天中价格最低时买入
#因此前i天的最大收益为前i-1天的最大收益和第i天卖出股票的最大收益间较大的值
#即，最后一天的价格-前i-1天的最小值
#递归关系为：maxProfit()= max(最后一天价格 - min(前i天价格), maxProfit(i-1))

#另外可以对一些特殊情况加一些特殊处理，可以减少时间开销
#例如，当有连续多天的价格持平时，在这几天中的哪一天卖出结果都一样，
# 因此可以对连续价格不变的情况加一个去重，然后只计算一次即可

#执行用时 :844 ms, 在所有 Python3 提交中击败了5.21%的用户
#内存消耗 :22.4 MB, 在所有 Python3 提交中击败了5.32%的用户
def maxProfit1(prices) -> int:
    if len(prices) <= 1:
        return 0
    p = prices.pop()
    while (len(prices) >= 1):
        if (p == prices[-1]):
            prices.pop()
        else:
            break
    if len(prices) < 1:
        return 0
    if p <= min(prices):
        return maxProfit(prices)
    else:
        return max(p - min(prices), maxProfit(prices))
#改进思路：
#上面的方法虽然通过了，但运行结果可以看到，只超过了5%的人，说明此递归方法的效率仍不够高
#上诉递归方法中，如果我们能将每次运行的结果记录下来，便可以减少不少的重复运算
#例如，开一个列表，专门用来记录一下运算结果，第i位表示前i天的最大收益
# 第一天记为0，从第二天开始记录,这样最大收益的基础值就是0了
#运行证明直接这样运行与上面的递归思路一致，但省略了价格持平时的去重操作，
# 导致运行超过时间限制，未通过，仍需继续优化
def maxProfit2(prices) -> int:
    max_prof = [0]
    for i in range(1,len(prices)):
        max_prof.append(max(max_prof[i-1],prices[i]-min(prices[:i])))
    return max_prof[-1]
#继续优化：
#分析上一种运行方式，发现每次求最小值的过程也比较费时间
#啥也不说了，添加数组记录最小值，避免每次用min计算
#执行用时 :72 ms, 在所有 Python3 提交中击败了40.13%的用户
#内存消耗 :14.1 MB, 在所有 Python3 提交中击败了13.20%的用户
def maxProfit3(prices) -> int:
    max_prof = [0]
    min_pric = [prices[0]]
    for i in range(1, len(prices)):
        min_pric.append(prices[i] if prices[i]<min_pric[i-1] else min_pric[i-1])
        max_prof.append(max(max_prof[i - 1], prices[i] - min_pric[i-1]))
    return max_prof[-1]
#感觉还可以继续优化~
#继续加一下去重试试
#由于去重之后prices的长度就发生变化了，如果继续按之前的i作为指针计入循环，
#会出现list index out of range
#为了避免此情况，计算中的指针可改为手动移动，for循环直接遍历prices成员来实现循环
#也就是代码中的prices[j]=i
#执行用时 :64 ms, 在所有 Python3 提交中击败了69.71%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了90.09%的用户
def maxProfit(prices) -> int:
    if len(prices)<=1:
        return 0
    max_prof = [0]
    min_pric = prices[:1]
    j = 1
    for i in prices[1:]:
        #print(i, j,  prices, min_pric,max_prof)
        if i==prices[j-1]:
            prices.pop(j)
            continue
        min_pric.append(i if i<min_pric[j-1] else min_pric[j-1])
        max_prof.append(max(max_prof[j - 1], i - min_pric[j-1]))
        j += 1
    return max_prof[-1]

def main():
    p = [3,3,5,0,0,0,3,1,4]#[2,2,5]
    print(maxProfit(p))


if __name__ == '__main__':
    main()
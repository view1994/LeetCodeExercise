# -*- coding: utf-8 -*-
#
#思路1：
#动态规划：
#先排除最大值在开头和最小值在最后的情况，
#然后遍历所有的交易情况
#指针i表示第一次买入的时间，则卖出第一个股票的时间可用指针j来遍历
#i<j,若第j天的价格不大于第i天价格，亏本的交易还不如不交易，舍去
#若第j天的价格大于第i天价格，本次交易的收益可计入总收益
#以i买j卖的交易为基础的最大总收益为第一笔交易的利润加上第j天以后的最大总收益
#为了遍历到所有正交易情况的总利润，将每一种i，j组合的最大总收益加入数列中
#遍历完之后返回所有总收益的最大值即可
#i,j组合的最大总收益与第j天以后的最大总收益构成递归关系
#即，maxProfit1(p)=p[j]-p[i]+maxProfit1(p[j+1:])
#超出时间限制，未通过
def maxProfit1(prices) -> int:
    while prices:
        if max(prices) == prices[0]:
            prices.pop(0)
        else:
            break
    while prices:
        if min(prices) == prices[-1]:
            prices.pop(-1)
        else:
            break
    if prices == []:
        return 0
    else:
        ret = [0]
        l = len(prices)
        for i in range(l - 1):
            if max(prices[i:]) <= prices[i]:
                continue
            for j in range(i + 1, l):
                if prices[i] < prices[j]:
                    ret.append(prices[j] - prices[i] + maxProfit(prices[j + 1:]))
                    # print(i,j,ret)
        return max(ret)
#改进思路
#上一个方法超时是可想而知的，因此考虑通过引入一个数组来记录递归结果，降低时间复杂度
#但是在实践的过程中发现，由j向j+1的递归无法用数组记录下来，
#因为在做f(j)的运算时，f(j+1)的值还未计算出来
#所以上述方法的递归方向不可取，需要重新分析一个递归方向才行
#考虑从上诉思路的反方向来找递归关系试试
#i和j用来遍历最后一次交易的卖出和买入，那么最大收益则为最后一次的收益加上最后一次买入前的所有天的最大收益
#即maxProfit(p)= p[i]-p[j]+maxProfit(p[:i-1])
#这样就构成了指针降序的递归方向
#另外，①在最开始和结束时的价格持平时，怎样买卖都不会对总收益造成影响，
#因此可以先对数据的头尾去重
#②当最高价在第一天和最低价对结尾时，都不宜交易，因此也先排除开头的最大值和结尾的最小值
#以上两种情况都没有必要进入递归，在递归前先排除这两种情况可减少大量不必要的计算
#由此思路，再将递归结果改为数组记录，实现方式如下：
#执行通过：
#执行用时 :1512 ms, 在所有 Python3 提交中击败了7.38%的用户
#内存消耗 :13.7 MB, 在所有 Python3 提交中击败了98.40%的用户
def maxProfit2(prices) -> int:
    while len(prices) > 1:
        if prices[0] == prices[1]:
            prices.pop(0)
        elif prices[-1] == prices[-2]:
            prices.pop(-1)
        else:
            break
    while prices:
        if max(prices) == prices[0]:
            prices.pop(0)
        else:
            break
    while prices:
        if min(prices) == prices[-1]:
            prices.pop(-1)
        else:
            break
    l = len(prices)
    if l < 2:
        return 0
    elif l == 2:
        return 0 if prices[0] >= prices[1] else prices[1] - prices[0]
    else:
        max_p = [0]
        for i in range(1, l):
            t = [0]
            for j in range(i):
                if prices[i] > prices[j]:
                    if j == 0:
                        t.append(prices[i] - prices[j])
                    else:
                        t.append(prices[i] - prices[j] + max_p[j - 1])
                t.append(max_p[j])
                # print(max_p,i,j,t)
            max_p.append(max(t))
        return max_p[-1]

#优化方案：
#观察上面的代码发现，生成列表t和求列表t的最大值会占用较多的时间
#且t只是为了用来找当前ij组合情况下的最大值而设的，因此可以直接用一个变量记录最大值即可
#实现方式如下，运行通过，且时间有减少
#执行用时 :908 ms, 在所有 Python3 提交中击败了7.38%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了92.87%的用户
def maxProfit(prices) -> int:
    while len(prices) > 1:
        if prices[0] == prices[1]:
            prices.pop(0)
        elif prices[-1] == prices[-2]:
            prices.pop(-1)
        else:
            break
    while prices:
        if max(prices) == prices[0]:
            prices.pop(0)
        else:
            break
    while prices:
        if min(prices) == prices[-1]:
            prices.pop(-1)
        else:
            break
    l = len(prices)
    if l < 2:
        return 0
    elif l == 2:
        return 0 if prices[0] >= prices[1] else prices[1] - prices[0]
    else:
        max_p = [0]
        for i in range(1, l):
            t_max = 0
            for j in range(i):
                if prices[i] > prices[j]:
                    if j == 0:
                        t = prices[i] - prices[j]
                        t_max = t if t>t_max else t_max
                    else:
                        t = prices[i] - prices[j] + max_p[j - 1]
                        t_max = t if t > t_max else t_max
                t_max = max_p[j] if max_p[j] > t_max else t_max
                # print(max_p,i,j,t)
            max_p.append(t_max)
        return max_p[-1]

def main():
    p=[7,1,5,3,6,4]
    print(maxProfit(p))


if __name__ == '__main__':
    main()
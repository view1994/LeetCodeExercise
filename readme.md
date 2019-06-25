## readme.md

[TOC]

```
tanyashideMBP:LeetCode tanyashi$ pwd
/Users/tanyashi/py_projs/LeetCode
tanyashideMacBook-Pro:playLeetCode tanyashi$ tree
.
├── LC10_RegularExpressionMatching.py
├── LC11_ContainerWithMostWater.py
├── LC121_BestTimetoBuyAndSellStock.py
├── LC12_IntToRoman.py
├── LC13_RomanToInt.py
├── LC144_BinaryTreePreorderTraversal.py
├── LC14_longestCommonPrefix.py
├── LC15_3Sum.py
├── LC16._3SumClosest.py
├── LC17_LetterCombinationsOfAPhoneNumber.py
├── LC18_4Sum.py
├── LC20_ValidParentheses.py
├── LC214_ShrotestPalindrome.py
├── LC21_MergeTwoSortedLists.py
├── LC23_MergeKSortedLists.py
├── LC26_RemoveDuplicatesFromSortedArray.py
├── LC33_SearchInRotatedSortedArray.py
├── LC37_SudokuSolver.py
├── LC43_MultiplyStrings.py
├── LC456_132pattern.py
├── LC46_Permutations.py
├── LC4_MedianOfTwoSortedArrays.py
├── LC53_MaximumSubarray.py
├── LC54_SpiralMatrix.py
├── LC576_OutOfBoundaryPaths.py
├── LC59_SpiralMatrix\ II.py
├── LC5_LongestPalindromicSubstring.py
├── LC61_RotateList.py
├── LC62_UniquePaths.py
├── LC6_ZigZag\ Conversion.py
├── LC70_ClimbingStairs.py
├── LC756_PyramidTransitionMatrix.py
├── LC78Subsets.py
├── LC7_ReverseInteger.py
├── LC88_MergeSortedArray.py
├── LC89_GrayCode.py
├── LC8_StringToInteger.py
├── LC9_Palindrome\ Numbers.py
├── content.md
└── readme.md

0 directories, 40 files
```


---
LC4_MedianOfTwoSortedArrays.py
LC5_LongestPalindromicSubstring.py
LC6_ZigZag Conversion.py
LC7_ReverseInteger.py
LC8_StringToInteger.py
LC9_Palindrome Numbers.py

### LC10_RegularExpressionMatching.py
**10. 正则表达式匹配**
[【leetcode】正则表达式匹配](https://blog.csdn.net/view994/article/details/81507219)

**TOPIC**
---- from leetcode题库，NO.10 [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/description/)

给定一个字符串 s 和一个字符规律 p，请实现一个支持 '.' 和 '*' 的正则表达式匹配。
所谓匹配，是要涵盖 **整个** 字符串 s的，而不是部分字符串。

>'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素

>- s 可能为空，且只包含从 a-z 的小写字母。
- p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

**ANALYZE**：
本题虽然只匹配两种字符，但有这两种字符可组合出多种匹配情况，且由于`*`匹配时还需要组合前一个字符才能判断，导致每次匹配时从p中获取的字符数不确定。
为了避免这个问题，在开始匹配前，调用SwitchPattern(p)，将p中的`*`与其之前的字母组合一下，改造为大写字母的形式，将`.*`的组合改造成`^`的形式，这样就能够实现p中一个字符代表一种匹配方式了。
改造了匹配规则的形式后的匹配方式仍有多种，也就是s中的一个字符可能可以与p中的多个字符匹配，则需要分别对不同的匹配方式分类讨论，对s中的每个字符，每一种匹配方式都应当尝试匹配，若匹配成功一个字符，则可以由递归进入下一个字符的匹配流程，若递归中匹配失败，则需要继续尝试下一种匹配方式，直到匹配成功，直接向上返回True，或四种匹配方式都无法使本次匹配和递归结果匹配成功，返回False。

需要注意的是，每一次尝试匹配时，匹配失败后s和p本身可能已经被递归中的匹配过程改写了，因此在每次尝试新的匹配方式时都应该**深拷贝**s和p的值作为输入。

**KEYWORDS**：
**def SwitchPattern(p)：**
此函数用于对原字符规律 p做个预处理，将`*`和`.`翻译成他们所能表示的内容。
由于本题所处理的字符串s只包含小写字母，因此借用与小写字母对应的大写字母表示，即将`*`加其前面的字幕替换为了它前面字母的大写字母，p中的大写字母表示匹配0~n个其对应的小写字母。
当`*`前的字符是`.`时，将`*.`替换为`^`，用于表示匹配0~n个任意字母。
p中字符`.`仍表示匹配任意单个字符。

**def isUpWord(w):**
参数w为匹配规则p中的单个字符。
此函数用于判断参数w是否可以匹配多个字符，即判断w是否是大写字母或者`^`，若w为大写字母或`^`则返回True，否则w为小写字母或`.`，只能匹配单个字符，返回False。

**def pretreatment(sentence,pattern):**
此函数用于在每次匹配前判断s或p为空的情况，也是递归的基例，并在s和p都不为空时做每次匹配前的预处理。
分四种情况：
s和p均为空时，说明匹配结束，能匹配上，返回True；
s不空而p为空时，说明p匹配完后s仍有字符剩余无法匹配，匹配失败，返回False；
s为空而p不空时，说明字符串s已匹配完，判断p中是否仍有未匹配完的小写字母，若存在小写字母则匹配失败，返回False，若p中只剩大写字母，则可匹配完，返回true；
s和p均不为空时，说明仍需继续匹配，则为下一步匹配做预处理：取出s的第一个字符和p中可与其匹配的内容，p的开头如果是大写字母，则将连续的大写字母存入队列d中，并取出p中第一个小写字母或者`.`，将预处理后的数据全部返回。

**def Match1word(sentence,pattern):**
此函数用于匹配s中的第一个字符。
在预处理后，已取出了s的第一个待匹配的字符s0，和p中可与之匹配的字符p0和d。
>p0是p的第一个非大写字母的字符，包括小写字母或`.`；
d包含p开头的一连串大写字母或`^`，从p的第一个字符开始，到遇到第一个小写字母为止.

第一个字符的匹配有四种情况，分别对应match1()、match2()、match3()、match4()如下：

- s0与p0匹配，p0是小写字母；
- s0与p0匹配，p0是`.`；
- s0与d中的一个大写字母匹配；
- s0与d中的`^`匹配。

match1()~match4()依次匹配，若有任意一种匹配方式匹配成功，则递归到s中下一个字符的匹配。若四种方式都匹配不上，则说明匹配失败，返回false。

**def isMatch(s,p):**
此函数为此问题的调用接口。
将字符串s转换成列表的形式，并对原字符规律p做预处理后，进入一个字符一个字符匹配的递归流程。

其他的solution1~尝试失败的思路，要么是无法遍历全部的匹配方式，要么是运行超时。
**执行结果**
通过
执行用时 :748 ms, 在所有 Python3 提交中击败了23.73%的用户
内存消耗 :13.2 MB, 在所有 Python3 提交中击败了68.57%的用户

### LC11_ContainerWithMostWater.py
**11. 盛最多水的容器**
**TOPIC**
---- from leetcode题库，NO.11 [Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/)

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：不能倾斜容器，且 n 的值至少为 2。

**ANALYZE**：
本题最简单粗暴的方法是直接遍历全部点两两组合的情况，记录最大值即可。但实际这样做时间复杂度较高，考虑其他思路改进算法。

本题可用**动态规划**来实现。
基本的表达式: area = min(height[i], height[j]) * (j - i)。
使用两个指针分别从数列头和尾出发，向内移动，值小的指针向内移动，这样就减小了搜索空间。 因为面积取决于指针的距离与值小的值乘积，如果值大的值向内移动，距离一定减小，而求面积的另外一个乘数一定小于等于值小的值，因此面积一定减小，而我们要求最大的面积，因此值大的指针不动，而值小的指针向内移动遍历即可。
用这种方法可将时间复杂度降低到O（n）。

**KEYWORDS**:
**def maxArea1(height):**
本方法简单粗暴，需要遍历所有点的两两组合情况，因此时间复杂度为：
（n-1）+(n-2)+...+1=n*n(n-1)/2
时间复杂度为O（n^2）
空间复杂度为O（1）
本方法由于超时而不通过。

**def maxArea(height):**
本方法为**动态规划**实现。
①当数列height中数据量大于1时，从数列头和尾分别弹出一个值
②取两个值中较小的为高度，height剩余数据量加一为宽度，计算并记录当前的面积
③舍弃两个值中较小的那个，将较大的那个装回height中原处，继续下一轮计算。
**执行结果**:
通过
执行用时 :220 ms, 在所有 Python3 提交中击败了5.20%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了99.44%的用户

### LC12_IntToRoman.py
**12. 整数转罗马数字**
**TOPIC**
---- from leetcode题库，NO.12 [Integer to Roman](https://leetcode-cn.com/problems/integer-to-roman/)

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。


字符  |   数值
--    |--
I     |   1
V     |   5
X     |   10
L     |   50
C     |   100
D     |   500
M     |   1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

>I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


**ANALYZE**：
**KEYWORDS**
**执行结果**
通过


LC13_RomanToInt.py
LC14_longestCommonPrefix.py
LC15_3Sum.py
LC16._3SumClosest.py
LC17_LetterCombinationsOfAPhoneNumber.py
LC18_4Sum.py
LC20_ValidParentheses.py
LC21_MergeTwoSortedLists.py
LC23_MergeKSortedLists.py
LC26_RemoveDuplicatesFromSortedArray.py
LC33_SearchInRotatedSortedArray.py
LC37_SudokuSolver.py
LC43_MultiplyStrings.py
LC46_Permutations.py
LC53_MaximumSubarray.py
LC54_SpiralMatrix.py
LC59_SpiralMatrix II.py
LC61_RotateList.py
LC62_UniquePaths.py
LC70_ClimbingStairs.py
LC78Subsets.py
LC88_MergeSortedArray.py
LC89_GrayCode.py
### LC121_BestTimetoBuyAndSellStock.py
买卖股票的最佳时期
**TOPIC**
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意:你不能在买入股票前卖出股票。

**KEYWORDS**
动态规划，递归优化，数组去重
**ANALYZE**：
最初思路：**动态规划**
重点是找出前一天和当天最大收益间的关系，构成递归结构
也就是已知前i-1天的最大收益，如何求加上第i天的价格后的最大收益?
最后一天有两种情况：
1最后一天卖出股票，则最大收益应该在前i-1天中价格最低时买入，收益为最后一天的价格减前i-1天的最小值
2最后一天不卖出股票，则前i天的最大收益等于前i-1天的最大收益
两种情况都要考虑到，结果取两种情况的最大值即可。
因此前i天的最大收益为前i-1天的最大收益和第i天卖出股票的最大收益间较大的值
递归关系为：**maxProfit()= max(最后一天价格 - min(前i天价格), maxProfit(i-1))**

另外可以对一些特殊情况加一些特殊处理，可以减少时间开销
例如，当有连续多天的价格持平时，在这几天中的哪一天卖出结果都一样，因此可以对连续价格不变的情况加一个去重，然后只计算一次即可。
maxProfit1实现了以上思路，首次通过，但效率不高。

**改进思路：记录递归结果**：
上面的方法虽然通过了，但运行结果可以看到，只超过了5%的人，说明此递归方法的效率仍不够高。
上诉递归方法中，如果我们能将每次运行的结果记录下来，便可以减少不少的重复运算。
例如，开一个列表，专门用来记录一下运算结果，第i位表示前i天的最大收益：第一天记为0，从第二天开始记录,这样最大收益的基础值就是0了。
运行maxProfit2证明直接这样运行与上面的递归思路一致，但省略了价格持平时的去重操作，导致运行超过时间限制，未通过，仍需继续优化。

**继续优化：记录最小值**
分析maxProfit2运行方式，发现每次求最小值的过程也比较费时间。其实可以跟优化递归一样，开个变量专门记录前i天的最小值。啥也不说了，添加数组记录最小值，避免每次用min计算。maxProfit3通过了测试，执行用时和内存消耗节省不少，说明优化的方向是可行的。

**感觉还可以继续优化~继续加一下去重试试**
由于去重之后prices的长度就发生变化了，如果继续按之前的i作为指针计入循环，会出现list index out of range
为了避免此情况，计算中的指针可改为手动移动，for循环直接遍历prices成员来实现循环，也就是代码中的prices[j]=i
maxProfit实现了加去重之后再递归，通过测试，并且时间和空间复杂度也都略有提升，(o゜▽゜)o☆[BINGO!]

**执行结果**
maxProfit1(prices)通过
>执行用时 :844 ms, 在所有 Python3 提交中击败了5.21%的用户
内存消耗 :22.4 MB, 在所有 Python3 提交中击败了5.32%的用户

maxProfit2(prices)运行超过时间限制，未通过

maxProfit3(prices)通过
>执行用时 :72 ms, 在所有 Python3 提交中击败了40.13%的用户
内存消耗 :14.1 MB, 在所有 Python3 提交中击败了13.20%的用户

maxProfit(prices)
>执行用时 :64 ms, 在所有 Python3 提交中击败了69.71%的用户
内存消耗 :13.8 MB, 在所有 Python3 提交中击败了90.09%的用户

---
LC144_BinaryTreePreorderTraversal.py
LC214_ShrotestPalindrome.py
LC456_132pattern.py
### LC576_OutOfBoundaryPaths.py
出界的路径数
https://blog.csdn.net/view994/article/details/80652426

LC756_PyramidTransitionMatrix.py

##content 
[toc]

```
tanyashideMBP:LeetCode tanyashi$ pwd
/Users/tanyashi/py_projs/LeetCode
tanyashideMBP:LeetCode tanyashi$ tree
.
├── LC10_isMatch.py
├── LC11_maxArea.py
├── LC12_IntToRoman.py
├── LC13_RomanToInt.py
├── LC144_BinaryTreePreorderTraversal.py
├── LC14_longestCommonPrefix.py
├── LC15_3Sum.py
├── LC17_LetterCombinationsOfAPhoneNumber.py
├── LC18_fourSum.py
├── LC20_ValidParentheses.py
├── LC214_ShrotestPalindrome.py
├── LC21_MergeTwoSortedLists.py
├── LC37_SudokuSolver.py
├── LC456_pattern\ 132.py
├── LC4_MedianOfTwoSortedArrays.py
├── LC576_OutOfBoundaryPaths.py
├── LC5_LongestPalindromicSubstring.py
├── LC6_ZigZag\ Conversion.py
├── LC756_PyramidTransitionMatrix.py
├── LC7_ReverseInteger.py
├── LC8_StringToInteger.py
├── LC9_Palindrome\ Numbers.py
├── content.md
└── readme.md

0 directories, 24 files


.
|____.git
|____.idea
|____content.md
|____LC10_RegularExpressionMatching.py
|____LC11_maxArea.py
|____LC12_IntToRoman.py
|____LC13_RomanToInt.py
|____LC144_BinaryTreePreorderTraversal.py
|____LC14_longestCommonPrefix.py
|____LC15_3Sum.py
|____LC16._3SumClosest.py
|____LC17_LetterCombinationsOfAPhoneNumber.py
|____LC18_fourSum.py
|____LC20_ValidParentheses.py
|____LC214_ShrotestPalindrome.py
|____LC21_MergeTwoSortedLists.py
|____LC23_MergeKSortedLists.py
|____LC26_RemoveDuplicatesFromSortedArray.py
|____LC33_SearchInRotatedSortedArray.py
|____LC37_SudokuSolver.py
|____LC43_MultiplyStrings.py
|____LC456_pattern 132.py
|____LC46_Permutations.py
|____LC4_MedianOfTwoSortedArrays.py
|____LC53_MaximumSubarray.py
|____LC54_SpiralMatrix.py
|____LC576_OutOfBoundaryPaths.py
|____LC59_SpiralMatrix II.py
|____LC5_LongestPalindromicSubstring.py
|____LC61_RotateList.py
|____LC62_UniquePaths.py
|____LC6_ZigZag Conversion.py
|____LC70_ClimbingStairs.py
|____LC756_PyramidTransitionMatrix.py
|____LC78Subsets.py
|____LC7_ReverseInteger.py
|____LC88_MergeSortedArray.py
|____LC89_GrayCode.py
|____LC8_StringToInteger.py
|____LC9_Palindrome Numbers.py
|____readme.md
|____test_git

```


---
### |____LC10_RegularExpressionMatching.py
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

### |____LC11_ContainerWithMostWater.py
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
本方法为动态规划实现。
①当数列height中数据量大于1时，从数列头和尾分别弹出一个值
②取两个值中较小的为高度，height剩余数据量加一为宽度，计算并记录当前的面积
③舍弃两个值中较小的那个，将较大的那个装回height中原处，继续下一轮计算。
**执行结果**:
通过
执行用时 :220 ms, 在所有 Python3 提交中击败了5.20%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了99.44%的用户

### |____LC12_IntToRoman.py
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

### |____LC13_RomanToInt.py
### |____LC144_BinaryTreePreorderTraversal.py
### |____LC14_longestCommonPrefix.py
### |____LC15_3Sum.py
### |____LC16._3SumClosest.py
### |____LC17_LetterCombinationsOfAPhoneNumber.py
### |____LC18_4Sum.py
### |____LC20_ValidParentheses.py
### |____LC214_ShrotestPalindrome.py
### |____LC21_MergeTwoSortedLists.py
### |____LC23_MergeKSortedLists.py
### |____LC26_RemoveDuplicatesFromSortedArray.py
### |____LC33_SearchInRotatedSortedArray.py
### |____LC37_SudokuSolver.py
### |____LC43_MultiplyStrings.py
### |____LC456_132pattern.py
### |____LC46_Permutations.py
### |____LC4_MedianOfTwoSortedArrays.py
### |____LC53_MaximumSubarray.py
### |____LC54_SpiralMatrix.py
### |____LC576_OutOfBoundaryPaths.py
### |____LC59_SpiralMatrix II.py
### |____LC5_LongestPalindromicSubstring.py
### |____LC61_RotateList.py
### |____LC62_UniquePaths.py
### |____LC6_ZigZag Conversion.py
### |____LC70_ClimbingStairs.py
### |____LC756_PyramidTransitionMatrix.py
### |____LC78Subsets.py
### |____LC7_ReverseInteger.py
### |____LC88_MergeSortedArray.py
### |____LC89_GrayCode.py
### |____LC8_StringToInteger.py
### |____LC9_Palindrome Numbers.py


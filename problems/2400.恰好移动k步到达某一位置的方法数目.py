# https://leetcode.cn/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/

# 给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。

# 给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。

# 如果所执行移动的顺序不完全相同，则认为两种方法不同。

# 注意：数轴包含负整数。

 

# 示例 1：

# 输入：startPos = 1, endPos = 2, k = 3
# 输出：3
# 解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
# - 1 -> 2 -> 3 -> 2.
# - 1 -> 2 -> 1 -> 2.
# - 1 -> 0 -> 1 -> 2.
# 可以证明不存在其他方法，所以返回 3 。

class Solution:
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """
        思路：数学-排列组合
        """
        startPos, endPos = (startPos, endPos) if endPos >= startPos else (endPos, startPos)
        distance = endPos-startPos
        if distance > k:
            return 0
        if distance == k:
            return 1
        if (k - distance) % 2 == 1: # 如果distance和k的差为奇数
            return 0
        # 为偶数的情况下，挑一半的step向前移动，一半向后移动互相抵消
        minus_steps = (k - distance)//2
        
        def factorial(n):
            # 实现阶乘
            if n == 0:
                return 1
            return n * factorial(n-1)
        # c(k, minus_steps): 选择向后移动的具体是哪些step
        return factorial(k)//(factorial(minus_steps)*factorial(k-minus_steps)) %(10**9+7)
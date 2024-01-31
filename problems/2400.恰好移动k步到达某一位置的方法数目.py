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
    def numberOfWays1(self, startPos: int, endPos: int, k: int) -> int:
        """
        思路：动态规划 + 记忆化搜索
        dp[x][left] 表示 在位置x，还有left步要走
        注意：这里有个难点是 x可能是负值，所以不太好用 二维数组进行存储，需要用字典存储 或者直接使用 functools.cache

        在Python的functools库中，@cache装饰器没有限制可以缓存的结果数量。换句话说，它会继续缓存结果，直到你的程序运行的系统内存用完为止。
        因此，在使用@cache装饰器时，你需要注意确保你的函数不会生成大量的唯一调用，这可能导致内存的快速消耗。
        在某些情况下，你可能想要限制缓存的大小。Python的functools.lru_cache装饰器可以让你指定一个最大的缓存大小。
        """
        lookup = {}
        def dp(x, left):
            """
            x：当前所在位置
            left: 还剩下的步数
            """
            if (x, left) in lookup:
                return lookup[(x, left)]
            if abs(x-endPos) > left:
                return 0
            if left == 0:
                return 1
            result = (dp(x-1, left-1)+dp(x+1, left-1)) % (10**9+7)
            lookup[(x, left)] = result
            return result
        # 等价于
        # from functools import cache
        # @cache
        # def dp(x, left):
        #     """
        #     x：当前所在位置
        #     left: 还剩下的步数
        #     """
        #     if abs(x-endPos) > left:
        #         return 0
        #     if left == 0:
        #         return 1
        #     result = (dp(x-1, left-1)+dp(x+1, left-1)) % (10**9+7)
        #     return result
        return dp(startPos, k)

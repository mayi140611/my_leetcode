# https://leetcode.cn/problems/power-of-two/description/
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

 

# 示例 1：

# 输入：n = 1
# 输出：true
# 解释：20 = 1

# 示例 2：

# 输入：n = 16
# 输出：true
# 解释：24 = 16


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """最优解: 检测n在过程中如果是奇数，就退出"""
        if n <= 0: return False
        if n == 1: return True
        while n > 1:
            if n % 2 == 1:
                return False
            n //= 2
        return True
    def isPowerOfTwo1(self, n: int) -> bool:
        """二分法"""
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            r = 2 ** mid
            if r == n:
                return True
            if r < n:
                if left == mid:
                    break
                left = mid
            else:
                right = mid
        if 2 ** left == n:
            return True
        return False
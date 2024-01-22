# https://leetcode.cn/problems/sqrtx/description/

# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

 

# 示例 1：

# 输入：x = 4
# 输出：2

# 示例 2：

# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        最佳思路：二分法
        """
        left, right = 0, x+1
        print(x)
        while left < right:
            mid = (left+right)//2
            r = mid ** 2
            if r == x:
                return mid
            if r < x:
                if left == mid: break # note: 边界，不然会陷入死循环
                left = mid
            else:
                right = mid
        return left-1 if left**2>x else left

assert Solution().mySqrt(x=4)==2
assert Solution().mySqrt(x=8)==2
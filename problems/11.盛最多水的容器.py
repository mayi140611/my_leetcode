# https://leetcode.cn/problems/container-with-most-water/description/
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 返回容器可以储存的最大水量。

# 说明：你不能倾斜容器。

# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

# 示例 2：

# 输入：height = [1,1]
# 输出：1

class Solution:

    def maxArea1(self, height: List[int]) -> int:
        """
        双指针
        执行用时分布
129ms
击败84.09%使用 Python3 的用户
消耗内存分布
26.67MB
击败35.90%使用 Python3 的用户
        """
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
    def maxArea(self, height: List[int]) -> int:
        """
        优化版
        执行用时分布
77ms
击败96.46%使用 Python3 的用户
消耗内存分布
27.03MB
击败29.75%使用 Python3 的用户
        """
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            if area > max_area:
                max_area = area
            cnt = 1
            if height[left] < height[right]:
                # 如果移动后的值 小于之前的值，计算的面积肯定更小，直接跳过
                while left+cnt<right and height[left+cnt] <= height[left]:
                    cnt += 1 
                left += cnt
            else:
                while right-cnt>left and height[right-cnt] <= height[right]:
                    cnt += 1 
                right -= cnt
        return max_area


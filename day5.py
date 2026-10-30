# 搜索插入位置
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:    # 当 left <= right 时，说明搜索区间还有元素
            mid = left + (right - left) // 2     # 相当于 (left + right) // 2，但这样写防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # 目标在右边，收缩左边界
            else:
                right = mid - 1  # 目标在左边，收缩右边界
        return left  # 循环结束时，left 就是目标应该插入的位置

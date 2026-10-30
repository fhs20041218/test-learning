# 移除元素（双指针）
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
        return slow
# 此解法用双指针，因为内部要进行增删改查等操作并且会进行迭代，所以在程序中用双指针

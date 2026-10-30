# 删除有序数组中的重复项
  class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = len(nums)
        fast = slow = 1 # 因为默认nums[0]是不重复元素，所以从1开始
        # fast是动态指针是会变的
        # slow永远指向下一个需要填入不重复元素的位置
        while fast < count: # 当数组中的数字个数大于1时一直循环
            if nums[fast] != nums[fast - 1]: # 如果在数组中索引为1的数字不等于索引在他的前面的数字时
                nums[slow] = nums[fast] # 那么就把该数字赋值给nums[slow]
                slow += 1
            fast += 1 # 无论有没有发现新元素，fast都要无条件向前走一步
        return slow

# 移除元素（值）
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for num in nums:  # Python 在 for fast in nums: 时，底层会创建一个迭代器
            if num != val:
                nums[slow] = num
                slow +=1
        return slow
# 此方法用值进行运算，此方法可读性高，但是迭代器就会错乱甚至报错导致崩溃，所以适用于脚本

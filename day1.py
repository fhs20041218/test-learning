# 两数相加
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 用字典存储 数值:索引
        num_map = {}
        for index, num in enumerate(nums):
            # 计算需要的另一个数
            complement = target - num
            # 如果这个数已经在字典里，说明找到了答案
            if complement in num_map:
                return [num_map[complement], index]
            # 否则把当前数和索引存进字典
            num_map[num] = index
        return []

# 最长公共前缀
  class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      length = len(strs[0])
      count = len(strs)
      if not strs:
        return ""
      for i in range(length):
        c = strs[0][i]
        for j in range(1,count):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]
      return strs[0]

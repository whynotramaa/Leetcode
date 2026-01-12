class Solution:
    def subarraySumWithAllPositives(self, nums: List[int], k: int) -> int:
        res = 0
        start, max_len = 0,0

        for end in range(len(nums)):
            res += nums[end]
            while res > k and start<=end:
                res -= nums[start]
                start+=1
            if res == k:
                length = end-start+1
                max_len = max(max_len, length)
        return max_len

class Solution:
    def subarraySumEqualKWithNegatives(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = {0:-1}

        for i in range(len(nums)):
            prefix+=nums[i]

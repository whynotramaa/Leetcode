# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            x = target - num
            if x in seen:
                return [seen[x], i]
            seen[num] = i
        return False

# sort colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low, mid = 0,0
        high = len(nums)-1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

# Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate

# Best time to buy and sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minii = prices[0]
        maxii = 0
        for i in range(len(prices)):
            minii = min(prices[i], minii)
            profit = prices[i] - minii
            maxii = max(profit, maxii)
        return maxii

# kadane algo
class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]
        for num in nums:
            current_sum = max(current_sum+num, num)
            max_sum = max(current_sum, max_sum)
        return max_sum

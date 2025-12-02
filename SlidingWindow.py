class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len

# max number of ones with at most k zeroes
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        count = 0

        for right in range(len(nums)):
            if nums[right]==0:
                count+=1
            while count>k:
                if nums[left] == 0:
                    count-=1
                left+=1

            max_len = max(max_len, right-left+1)
        return max_len


# 2 baskets and max amount of fruits that can be kept
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        basket = {}
        max_len = 0

        for right in range(fruits):
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit,0)+1

            while len(basket)>2:
                basket[fruits[left]]-=1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left+=1

            max_len = max(max_len, right-left+1)

        return max_len

# Longest repeating char replacement



# Subarrays with sum == goal

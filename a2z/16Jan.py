# Next Permutations
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            nums.reverse()
            return
        j = n-1
        while nums[j]<=nums[i]:
            j-=1

        nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = reversed(nums[i+1:])
        return nums

# leaders in an array
class Solution:
    def leaders(self, nums: List[int]) -> None:
        maxx = nums[-1]
        leaders = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= maxx:
                leaders.append(nums[i])
                maxx = nums[i]
        return leaders # if we need to preserve order, reverse the list

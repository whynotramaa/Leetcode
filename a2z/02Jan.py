# Check if array is sorted and rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i in range(1,len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                count+=1

            if nums[0] < nums[-1]:
                count+=1

        return count <= 1

# Second Largest Element
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first_largest =  arr[0]
        second_largest = -1
        for num in arr:
            if num > first_largest:
                second_largest = first_largest
                first_largest = num
            elif num > second_largest and num < first_largest:
                second_largest = num

        return second_largest


# remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1

        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[idx] = nums[i]
                idx+=1

        return idx

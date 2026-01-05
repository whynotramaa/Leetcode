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

# ROTATION OF AN ARRAY
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k%len(nums)
        # if k==0:
        #     return
        # nums1 = nums[-k:]
        # nums2 = nums[:-k]
        # nums[:] = nums1 + nums2

        def reverse(arr,left,right):
            while left<right:
                arr[left], arr[right] = arr[right], arr[left]
                left+=1
                right-=1

        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

        return nums


# Move zeroes to end
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # in-place modification please
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastNonZero] = nums[i]
                if lastNonZero!=i:
                    nums[i]=0
                lastNonZero+=1
        return nums


# Union of two arrays
class Solution:
    def findUnique(arr1,arr2):
        map_dict = defaultdict(int)
        for x in arr1:
            map_dict[x] += 1 # same as freq[x] = freq.get(freq[x],0) + 1
        for y in arr2:
            map_dict[y] += 1
        result = sorted(map_dict.keys)


# missing number => total_sum - arthimetic_sum
# max consecutive ones => [1,1,0,1,1,1,1,0,1,1,1] -- count and if nums[i] == 0, max_count = max(...) and count = 0


# find single number - every elem appears twice except one
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

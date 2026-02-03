class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1

        return False

# SEARCH IN ROTATED SORTED ARRAY 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1


# SEARCH IN ROTATED SORTED ARRAY 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            if nums[low] == nums[mid] == nums[high]:
                low+=1
                high-=1
                continue

            if nums[low] <= nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

# MIN in rotated sorted arr
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = float('inf')
        while low<=high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid+1
            else:
                ans = min(ans,nums[mid])
                high = mid-1

        return int(ans)


# Rotation Count
class Solution:
    def rotationCount(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = 0
        while low<=high:
            mid = (low+high)//2

            if nums[low] <= nums[high]:
                ans = low
                break

            if nums[low] <= nums[mid]:
                ans = low
                low = mid+1
            else:
                ans = mid
                high = mid-1

        return ans



# finding peak elem
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low<high:
            mid = (low+high)//2

            if nums[mid] < nums[mid+1]:
                low=mid+1
            else:
                high = mid

        return low

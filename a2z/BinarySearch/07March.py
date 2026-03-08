class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j-=1
            
            nums[i], nums[j] = nums[j], nums[i]

        nums[i+1:] = reversed(nums[i+1:])

def leaders_in_array(arr):
    res = []
    max_right = float('-inf')

    for i in range(len(arr)-1,-1,-1):
        if arr[i] >= max_right:
            res.append(arr[i])
            max_right = arr[i]
    
    return res[::-1]


def longest_seq(nums):
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if (num-1) not in num_set:
            curr = num
            streak = 1

            while(curr+1) in num_set:
                curr+=1
                streak+=1

            max_len = max(max_len, streak)
    
    return max_len


def subarr_sum(nums,k):
        prefix = {0:1}
        count = 0
        curr = 0

        for num in nums:
            curr += num
            if curr-k in prefix:
                count += prefix[curr-k]

            prefix[curr] = prefix.get(curr, 0) + 1
        
        return count

def book_allocation(pages, m):
    if m > len(pages):
        return -1
    
    def is_possible(mid):
        students = 1
        curr = 0

        for p in pages:
            if curr + p <= mid:
                curr += p
            else:
                students += 1
                curr = p

                if students > m:
                    return False
        return True
    
    low = max(pages)
    high = sum(pages)

    while low<=high:
        mid = (low+high)//2

        if is_possible(mid):
            high = mid-1
        else:
            low = mid+1

    return low


def max_subarr_sum(nums, k):

    def is_possible(limit):
        splits = 1
        curr = 0

        for num in nums:
            if num + curr <= limit:
                curr += num
            
            else:
                splits += 1
                curr = num
                if splits > k:
                    return False
                
        return True
    
    low = max(nums)
    high = sum(nums)

    while low<=high:
        mid = (low+high)//2

        if is_possible(mid):
            high = mid-1
        else:
            low = mid+1
    
    return low


def minimise_max_gap(stations, k):
    def required(d):
        count = 0
        for i in range(1, len(stations)):
            gap = stations[i] - stations[i-1]
            count += int(gap/d)
            if gap % d == 0:
                count -= 1
        return count
    
    low = 0
    high = stations[-1] - stations[0]

    while high-low > 1e-6:
        mid = (low+high) / 2

        if required(mid) <= k:
            high = mid
        else:
            low = mid
    
    return high



class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def is_possible(d):
            total = 0
            for num in nums:
                total += (num + d - 1) // d
            return total<=threshold
        
        low = 1
        high = max(nums)
        ans = high

        while low<=high:
            mid = (low+high)//2

            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 

        return ans
    
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(c):
            day = 1
            curr = 0

            for w in weights:
                if w + curr > c :
                    day+=1
                    curr = w
                else:
                    curr += w

            return day <= days
        
        low = max(weights)
        high = sum(weights)

        while low<=high:
            mid = (low+high)//2

            if is_possible(mid):
                high = mid-1
            else:
                low=mid+1

        return low
        
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1

        while low<=high:
            mid = (low+high)//2

            missing = arr[mid] - (mid+1)

            if missing<k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k


def aggressiveCows(stalls, k):
    stalls.sort()

    def is_possible(dist):
        last_pos = stalls[0]
        count = 1

        for i in range(1,len(stalls)):
            if stalls[i] - last_pos >= dist:
                count+=1
                last_pos = stalls[i]
            
            if count >= k:
                return True
        
        return False
    
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0

    while low <= high:
        mid = (low+high)//2

        if is_possible(mid):
            ans = mid
            low = mid+1
        else:
            high = mid-1

    return ans


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)-1
        if m*k>n:
            return -1
        def is_possible(d):
            bouquet = 0
            count = 0
            for b in bloomDay:
                if d >= b:
                    count += 1
                    if count == k:
                        bouquet += 1
                        count = 0
                else:
                    count = 0
            return bouquet >= m
        
        low = min(bloomDay)
        high = max(bloomDay)

        while low<=high:
            mid = (low+high)//2

            if is_possible(mid):
                high = mid-1
            else:
                low = mid+1
        return low

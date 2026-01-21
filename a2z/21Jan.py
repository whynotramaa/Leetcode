# pascal triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle


# majorityElement > n/3 items
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+=1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1-=1
                count2-=1

        count1 = count2 = 0

        for number in nums:
            if number == candidate1:
                count1+=1
            elif number == candidate2:
                count2+=1

        ans = []

        if count1 > len(nums)//3:
            ans.append(candidate1)
        if count2 > len(nums)//3:
            ans.append(candidate2)

        return ans

# three sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left,right = i+1, len(nums)-1

            while left<right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1

        return res

# four sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left,right = j+1, len(nums)-1

                while left<right:
                    total = nums[left] + nums[right] + nums[j] + nums[i]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right-=1

                        left+=1
                        right-=1

                    elif total < target:
                        left+=1
                    else:
                        right-=1

        return res

# max prod subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_prod, min_prod, res = nums[0], nums[0], nums[0]

        for i in range(1,len(nums)):
            curr_max = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            curr_min = min(nums[i], max_prod*nums[i], min_prod*nums[i])

            max_prod, min_prod = curr_max, curr_min

            res = max(res, max_prod)

        return res

# subarray sum equals K
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}

        for num in nums:
            prefix+=num

            if prefix - k in freq:
                count += freq[prefix-k]

            freq[prefix] = freq.get(prefix,0)+1

        return count

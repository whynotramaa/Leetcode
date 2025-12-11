
# QUESTIONS INCLUDED - secons set of 5 qns of neetcode 150
# productExceptSelf
# isValidSudoku
# longestConsecutiveSequence
# isValidPalindrome
# twoSumOfSortedArrays




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do it in 2 pass, 1 prefix and then 1 suffix, it would automatically exclude the ith element itself as we are mutliplying from
        # there to last for once and form there too begining, not including that at any place

        prefix = [1]*len(nums)
        res = [1]*len(nums)

        for i in range(1,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]

        # right = [1] * len(nums)
        # for j in range(len(nums)-2,-1,-1):
        #     right[j] = nums[j+1]*right[j+1]
        # for k in range(len(nums)):
        #     res[k] = left[k] * right[k]

        suffix = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] = prefix[j]*suffix
            suffix = suffix * nums[j]

        return res



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                box_index = (r//3)*3 + (c//3)
                val = board[r][c]
                if val == ".":
                    continue

                if ( val in row[r] or val in col[c] or val in box[box_index] ):
                    return False

                row[r].add(val)
                col[c].add(val)
                box[box_index].add(val)

        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for num in seen:
            if num-1 not in seen:
                current = num
                length = 1
                while current+1 in seen:
                    current+=1
                    length+=1
                max_len = max(max_len, length)

        return max_len

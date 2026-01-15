# alternate polarity
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # take an array with 2 indexes running pos and neg
        arr = [0]*len(nums)
        posIndex, negIndex = 0,1

        for num in nums:
            if num > 0:
                arr[posIndex] = num
                posIndex+=2
            else:
                arr[negIndex] = num
                negIndex+=2
        return arr

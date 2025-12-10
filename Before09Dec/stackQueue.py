class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ')':'(', '}':'{', ']':'[' }

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if not stack or stack[-1]!=pairs[c]:
                    return false
                stack.pop()
        return len(stack)==0

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val,val])
        else:
            current_min = self.stack[-1][1]
            self.stack.append([val, min(current_min, val)])


    def pop(self) -> None:
        if not self.stack:
            raise IndexError("Stack is empty")
        else:
            self.stack.pop()


    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack= []
        nge = {}

        for i in range(len(nums2)-1,-1,-1):
            curr_elem = nums2[i]
            while stack and stack[-1]<=curr_elem:
                stack.pop()
            if stack:
                nge[curr_elem] = stack[-1]
            else:
                nge[curr_elem]=-1

            stack.append(curr_elem)

        return [nge[num] for num in nums1]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)

        for i in range(2*len(nums)-1,-1,-1):
            current = nums[i%len(nums)]
            while stack and stack[-1]<=current:
                stack.pop()
            if i<len(nums):
                if stack:
                    res[i] = stack[-1]
            stack.append(current)
        return res

        # CIRCULAR NEXT SMALLER
class Solution:
    def nextSmallerElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums)

        for i in range(2*len(nums)-1,-1,-1):
            current = nums[i%len(nums)]
            while stack and stack[-1] >= current:
                stack.pop()
            if i<len(nums):
                if stack:
                    res[i] = stack[-1]
            stack.append(current)
        return res


class Solution:
    def deleteMiddleFromStack(self, nums):
        res  = []
        n = len(stack)
        target = n//2
        temp = []

        for i in range(n):
            if i != target:
                temp.append(stack.pop())

        return temp[::-1]

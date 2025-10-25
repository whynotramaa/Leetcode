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

# QUESTIONS INCLUDED - first 6 qns of neetcode 150
# containsDuplicate
# validAnagram
# twoSum
# groupAnagrams
# topKfrequentElements
# encodeAndDecodeStrings


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        # return len(set(nums)) != len(nums)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # tt = sorted(list(t))
        # aa = sorted(list(s))

        # if tt == aa:
        #     return True
        # return False


        # return Counter(s) == Counter(t)

        if len(s)!=len(t):
            return False
        count = {}

        for str in s:
            count[str] = count.get(str,0)+1

        for char in t:
            if char not in count:
                return False
            if char in count:
                count[char] -= 1
                if count[char] == 0:
                    del count[char]

        return len(count)==0


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(nums):
            x = target - num  # target will always be bigger than num
            if x in seen:
                return [seen[x],i]
            seen[num] = i     # we dont have add in dict and we need to save index of number not x
        return False


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        # for word in strs:
        #     key = ''.join(sorted(word))
        #     groups[key].append(word)

        # return list(groups.values())

        for word in strs:
            freq = [0]*26
            for ch in word:
                freq[ord(ch)-ord('a')] += 1

            key = tuple(freq)
            groups[key].append(word)

        return list(groups.values())

        # if signature not in groups:
        #     groups[signature] = []
        # groups[signature].append(word)

        # instead of all this we are using defaultdict to make a new empty list whenever a key is accessed

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(list)

        for num in nums:
            count[num] = count.get(num,0)+1 #cannot do direct +1 because at first it will be []

        sort_counts = sorted(count.items(), key= lambda x:x[1], reverse=True)
        # count = {1:3, 2:1, 3:5}   and   count.items() = [(1,3),(2,1),(3,5)]   so sorting count will not work.

        # this will return [(value1,freq1), (value2,freq2), ... ]
        return [item[0] for item in sort_counts[:k]]

        # count = Counter(nums)
        # return [num for num,freq in count.most_common(k)]


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])

            start = j+1
            end = j+1+length

            decoded.append(s[start:end])

            i = end
        return decoded

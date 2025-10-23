class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int) #bcz i am counting frequency
        for num in nums:
            count[num]+=1
        # count.sorted() --> this is not an array
        # return count[:k]

        sort_count = sorted(count.items(), key = lambda x: x[1], reverse = True)

        return [item[0] for item in sort_count[:k]]

        # we could have done the counter approach
        # count = Counter(nums)
        # return [num for num,freq in count.most_common(k)]
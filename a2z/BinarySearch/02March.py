# Finding nth root of m
def nthRoot(self, n, m):
    low = 1
    high = m

    if m == 0:
        return 0

    while low<=high:
        mid=(low+high)//2
        val = mid**n

        if val == m:
            return mid
        elif val>m:
            high = mid-1
        else:
            low = mid+1

    return -1



# koko eating bananas
def minEatingSpeed(piles,h):
    low = 1
    high = max(piles)
    ans = high

    while low<=high:
        mid = (low+high)//2

        hours = 0

        for p in piles:
            hours += (p + mid-1) // mid

        if hours <= h:
            ans = mid
            high = mid-1

        else:
            low = mid+1

    return ans



def min_days(bloomDay,m,k):
    n = len(bloomDay)

    if m*k > n:
        return -1
    
    def is_possible(day):
        bouq = 0
        curr = 0

        for b in bloomDay:
            if b<=day:
                curr+=1
                if curr == k:
                    bouq += 1
                    curr = 0 # because bouquet has been made
            else:
                curr = 0
        
        return bouq >= m
    
    low = 1
    high = max(bloomDay)

    ans = -1

    while low<=high:
        mid = (low+high)//2
        if is_possible(mid):
            ans = mid
            high = mid-1
        else:
            low = mid+1
    
    return ans


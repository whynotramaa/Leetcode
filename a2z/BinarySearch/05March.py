def majority_elem(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        
        if candidate == num:
            count+=1
        else:
            count-=1
    
    return candidate

def max_subarr_sum(arr):
    curr = 0
    max_sum = float('-inf')

    for num in arr:
        curr = max(num, curr+num)
        max_sum = max(max_sum, curr)
    
    return max_sum

def max_with_indices(arr):
    curr = 0
    max_sum = float('-inf')

    start = 0
    left,right = 0,0

    for i,num in enumerate(arr):

        if num > curr+num:
            curr = num
            start = i
        else:
            curr += num

        if curr > max_sum:
            max_sum = curr
            left = start
            right = i
    
    return max_sum,left,right


def stock_buy_sell(prices):
    min_price = float('-inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)

    return max_profit


def rearrange_by_sign(arr):
    result = [0]*len(arr)
    pos_idx = 0
    neg_idx = 1

    for num in arr:
        if num>0:
            result[pos_idx] = num
            pos_idx+=2
        else:
            result[neg_idx] = num
            neg_idx+=2
    
    return result


def majority_2(arr):
    cand1, cand2 = None, None
    count1, count2 = 0, 0

    for num in arr:
        if cand1 == num:
            count1 += 1
        elif cand2 == num:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    
    res = []

    for cand in [cand1, cand2]:
        if arr.count(cand) > len(arr)//3:
            res.append(cand)
    
    return res
        
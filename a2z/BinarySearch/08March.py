def minimise_max_gap(stations, k):
    def required(d):
        count = 0
        for i in range(1, len(stations)):
            gap = stations[i] - stations[i-1]
            count += int(gap/d)
            if gap % d == 0:
                count -= 1
        return count
    
    low = 0
    high = stations[-1] - stations[0]

    while high-low > 1e-6:
        mid = (low+high) / 2

        if required(mid) <= k:
            high = mid
        else:
            low = mid
    
    return high
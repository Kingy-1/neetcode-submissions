class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Shortest amount of time (h) possible is len(piles)
            Occurs when we eat at a rate, k which is max(piles)
        
        this shows that max(piles) is the fastest possible eating rate giving us the shortest amount of time and 1 is hte slowest possible eating rate giving us the longest amount of time.

        Can use binary search since it is monotomous as k decreases h will always increase

        Start at 1
        end at max(piles)

        while start <= end:
            get the mid value and compute the time in hours
            
            If the time == 5:
                return mid
            if the time takes longer than 5:
                we want a faster rate so we increase k
                done by moving the start to mid + 1
            if the time is less than 5:
                we want a slower rate so we decrease k
                move end to mid - 1
        """

        start = 1
        end = max(piles)

        while start <= end:
            mid = (start + end) // 2
            time = 0
            
            for i in piles:
                time += math.ceil(i/mid)
            
            if time == h:
                end = mid - 1
            elif time > h:
                start = mid + 1
            elif time < h:
                end = mid - 1

        if time > h:
            return mid + 1
        return mid


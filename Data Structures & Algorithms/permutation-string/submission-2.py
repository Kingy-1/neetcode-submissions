class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        get key value pairs of s1 | seen1

        Search fixed windows of size len(s1)
        Move window forward until last element
        
        tracker = {}

        for every letter in window_size:
            add letter to tracker 
            
            if tracker[letter] > seen1[letter]:
                break
        
        if tracker == seen1:
            return True
        
        return False
        """

        if len(s1) > len(s2):
            return False
        
        seen1 = {}

        for i in s1:
            seen1[i] = seen1.get(i, 0) + 1
        
        l = 0
        start = len(s1)-1
        end = len(s2)

        for r in range(start, end):
            tracker = {}

            for i in range(l, r+1):
                tracker[s2[i]] = tracker.get(s2[i], 0) + 1

                if s2[i] not in seen1 or tracker[s2[i]] > seen1[s2[i]]:
                    break
            
            if tracker == seen1:
                return True
            
            l += 1
        
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        get key value pairs of s1 | seen1

        Search fixed windows of size len(s1)
        Move window forward until last element
        
        l = 0
        
        while r < len(s2):
            tracker = {}

            while s2[r] in seen1:
                tracker[s2[r]] = tracker.get(s2[r], 0) + 1
                
                if s2[r] not in seen1 or tracker[s2[r]] > seen1[s2[r]]:
                    break
                
                r += 1
            
            if tracker == seen:
                return True
            
            r += 1
        
        return False
        """

        if len(s1) > len(s2):
            return False
        
        seen1 = {}

        for i in s1:
            seen1[i] = seen1.get(i, 0) + 1
        
        r = 0
        l = 0
        
        while r < len(s2):
            tracker = {}
            
            while r < len(s2) and s2[r] in seen1:
                tracker[s2[r]] = tracker.get(s2[r], 0) + 1
                
                while tracker[s2[r]] > seen1[s2[r]]:
                    # we have a duplicate
                    
                    if s2[l] in tracker:
                        tracker[s2[l]] -= 1
                    
                    l += 1

                r += 1
            
                if tracker == seen1:
                    return True
                
            if r < len(s2) and s2[r] not in seen1:
                l = r
            
            r += 1
            l += 1
        
        return False

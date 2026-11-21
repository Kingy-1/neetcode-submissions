class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        dynamic + fixed window

        max_freq = largest num of time a char repeats in the dynamic window
        count = 0 | int we are returning

        dynamic window of size k + 1 since we can always replace k elements
        window_freq = {}
        window_size = r - l + 1
        
        while r < len(s):
            append current s[r] value and key to window_freq dict
            max_freq = max(window_freq) or max(window_freq.values())

            l stays at its current point

            dynamic window r pointer moves to the right until max_freq + k > window_size at which:

            if max_freq + k > window_size:
                count = max(window_size, count)
                while l < r or max_freq + k <= window_size:
                    subtract 1 from value at the key s[l] from window_freq
                    max_freq = max(window_freq) or max(window_freq.values())
                    l += 1
            else:
                r += 1
            
                
        """

        max_freq = 0 #largest num of time a char repeats in the dynamic window
        count = 0 #| int we are returning

        window_freq = {}
        l, r = 0, 0
        window_size = r - l
        
        while r < len(s):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            max_freq = max(window_freq.values())

            while max_freq + k < (r - l + 1):
                window_freq[s[l]] -= 1
                max_freq = max(window_freq.values())
                l += 1

            count = max(count, r - l + 1)
            r += 1
        
        return count
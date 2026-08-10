class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        s = s.lower()

        while left < right:
            # check if s[left] is a num 
            # if not increase left by 1 and continue
            # do the same for s[right] but instead decrease by 1
            # If they are both numbers
            # check if s[left] != s[right]
            # if so return False
            # otherwise decrease right by 1 and increase left by 1

            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start at end of digits
        # multiply end of digits by 10^(i+1) and add it to a running sum
        # continue until you reach the first number
        # add 1 to ans and turn ans into a list
        # return ans

        ans = []
        sums = []
        k = len(digits)-1

        for i in range(0, len(digits)):
            test = int(digits[i]) * (10**(k))
            sums.append(test)
            k -= 1
        sums[len(sums)-1] += 1

        look = str(sum(sums))

        for i in range(len(look)):
            print(look[i])
            ans.append(look[i])
        return ans

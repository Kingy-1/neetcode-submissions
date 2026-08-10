class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        create a set of numbers
        ans = []
        for i in range(len(number))

            check if target-number is in the data set
            if so append i to ans
                if so use linear search 
                for j in range(i+1, len(numbers))
                    check if value == target-number:
                        if so append j to ans
                        return ans
                        
        """

        ans = []
        check = set(numbers)

        for i in range(len(numbers)):
            if target-numbers[i] in check:
                ans.append(i+1)
                for j in range(i+1, len(numbers)):
                    if numbers[j] == target-numbers[i]:
                        ans.append(j+1)
                        return ans
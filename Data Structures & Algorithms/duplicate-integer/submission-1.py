class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an empty list
        # append to that list any new values
        # if the length of that array is different to nums return false
        # else return true

        empty:list = []


        length:int = len(nums)
        i:int = 0
        while(i<length):
            if(nums[i] not in empty):
                empty.append(nums[i])
            i += 1

        if(len(empty) < length):
            return True
        else:
            return False
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Create a defaultdict of type list
        This list will the ordered letters in each word as a key
        For each word in strs
            we are going to turn the word into a a tuple of sorted strings
            We require a tuple since it is immutable and we need an immutable
            datatype to act as a key

            this is because each anagram has the same group of sorted
            letters just in a different order
            
            we append the word since this keeps each value
            if we added s it unpacks s and adds each individual letter
            
        return the values of the dict
        """

        temp = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            temp[sorted_word].append(word)
                
        return list(temp.values())
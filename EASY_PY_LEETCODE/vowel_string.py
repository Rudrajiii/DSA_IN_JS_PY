from typing import *
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left , right+1):
            vowels = 'aeiou'
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
        return count 
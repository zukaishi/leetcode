print("arrayStringsAreEqual")

class Solution:
    def arrayStringsAreEqual(self, word1,word2) -> bool:
        return_bool = False
        if ''.join(word1) == ''.join(word2):
            return_bool = True
        return return_bool


word1 = ["ab", "c"]
word2 = ["a", "bc"]
solution = Solution()
print(solution.arrayStringsAreEqual(word1,word2))
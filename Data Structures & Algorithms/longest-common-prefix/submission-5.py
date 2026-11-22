class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix: str = ""
        first_word: str = strs[0]

        for char in first_word:
            if (all(common_prefix + char in word for word in strs)):
                common_prefix = common_prefix + char
            else:
                return common_prefix
        return common_prefix
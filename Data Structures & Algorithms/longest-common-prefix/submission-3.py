class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix: str = ""
        first_word: str = strs[0]
        words: List[str] = strs

        for index, char in enumerate(first_word):
            if (all(common_prefix + char in word for word in words)):
                common_prefix = common_prefix + char
            else:
                return common_prefix
        return common_prefix

# target = "app"
# words = ["apple", "application", "pineapple"]

# result = all(target in word for word in words)
# print(result)  # True
 
        


# U M P I R E 

# • U — Understand: Read the problem carefully, clarify inputs, outputs, constraints, and edge cases, and ask the interviewer questions before jumping into code.
# • M — Match: Relate the problem to known categories, patterns, or data structures (such as two pointers, sliding windows, hash maps, or dynamic programming).
# • P — Plan: Outline your approach using pseudocode or high-level steps, discussing brute-force options versus optimized solutions.
# • I — Implement: Write clean, working code while managing edge cases and talking through your logic.
# • R — Review: Trace your code manually using sample test cases and a variable "watchlist" to catch bugs or off-by-one errors.
# • E — Evaluate: Analyze and state the time complexity and space complexity of your solution, and discuss potential optimizations.
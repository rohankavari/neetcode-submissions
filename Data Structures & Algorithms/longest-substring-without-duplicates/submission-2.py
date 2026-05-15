class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def valid(s):
            return len(s) == len(set(s))

        l = 0
        r = 1
        longest = 0
        while r <= len(s) and l <= len(s):
            # print(s[l:r],valid(s[l:r]))
            if valid(s[l:r]):
                longest = max(longest,len(s[l:r]))
                r += 1
            else:
                l+=1

        return longest
            
'''
Goal: Given a string s, return the longest palindromic substring in s.

Note: My solution starts by finding a letter and expanding outwards both to the left and right and checking if they are equal chars.
If so then it is a palindrome and this is repeated till the case is False.
I do this as many times as possible and keep the longest palindrome I found thus far.
I must not forget to handle the edge case of a possible even number palindrome which is only possible for first two chars.

Currently working status: Am failing due to little edge cases I keep failing to consider. Might not be optimal but almost completed.
passed 88/143 test cases so far.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        longest = s[:2]
        middle = 1
        outwards = 1
        while middle < len(s)-1:
            if s[middle] == s[middle+1]:
                if len(longest) == len(s[middle:middle+2]):
                    longest = s[middle:middle+2]
            left = middle - outwards
            right = middle + outwards
            if right >= len(s):
                break
            if left < 0:
                left = 0

            if s[left] == s[right]: #check left and right chars that outwards amount of chars away from middle
                if len(s[left:right+1]) >= len(longest):
                    longest = s[left:right+1]
                outwards += 1

            else:
                outwards = 1
                middle += 1
        if len(longest) == 2:
            if longest[0] != longest[1]:
                return longest[0]

        return longest



def main():
    solution = Solution()
    # print(solution.longestPalindrome("babad"))
    # print(solution.longestPalindrome("cbbd"))
    # print(solution.longestPalindrome("abcba"))
    # print(solution.longestPalindrome("aaaa"))
    # print(solution.longestPalindrome("abcda"))
    print(solution.longestPalindrome("aaabaaaa"))
if __name__ == '__main__':
    main()
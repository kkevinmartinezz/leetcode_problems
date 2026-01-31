'''
Goal: Given a string s, return the longest palindromic substring in s.

Note: My solution starts by finding a letter and expanding outwards both to the left and right and checking if they are equal chars.
If so then it is a palindrome and this is repeated till the case is False.
I do this as many times as possible and keep the longest palindrome I found thus far.

I handle the edge case of it possibly being an even palindrome by doing the same method as above but this time starting with side by side letter.

Credit: NEETCODE helped me on this one, used his code to complete and understand where I was going wrong.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        longest_length = 0
        for i in range(len(s)): #Check regularly by expanding outwards, this ultimately checks odd length palindromes
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]: #check if in bounds and if left and right equate to same char
                if (r - l + 1) > longest_length: #if length is longer then existing known length of longest palindrome found so far
                    longest_length = r - l + 1 # length is now the subtraction of the left and right, 1 is added since index starts with 0 not 1
                    longest = s[l:r+1] #must add one to r since the right side is exclusive
                l -= 1
                r += 1

            #now copy same thing but starting with left and right being side by side chars
            #this will ultimately check for even type palindromes starting at the given i in for loop
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[
                r]:  # check if in bounds and if left and right equate to same char
                if (
                        r - l + 1) > longest_length:  # if length is longer then existing known length of longest palindrome found so far
                    longest_length = r - l + 1  # length is now the subtraction of the left and right, 1 is added since index starts with 0 not 1
                    longest = s[l:r + 1]  # must add one to r since the right side is exclusive
                l -= 1
                r += 1


        return longest



def main():
    solution = Solution()
    print(solution.longestPalindrome("babad"))
    print(solution.longestPalindrome("cbbd"))
    print(solution.longestPalindrome("abcba"))
    print(solution.longestPalindrome("aaaa"))
    print(solution.longestPalindrome("abcda"))
    print(solution.longestPalindrome("aaabaaaa"))
if __name__ == '__main__':
    main()
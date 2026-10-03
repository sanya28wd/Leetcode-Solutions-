class Solution(object):
    def isPalindrome(self, s):
        palindrome=True
        s=s.lower()
        new_string="".join([char for char in s if char.isalnum()])
        i = 0
        j=len(new_string)-1
        while i<j:
            if new_string[i]!=new_string[j]:
                palindrome=False
            i+=1
            j-=1
        return palindrome
        
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        if n<=1:
            return ''
        list_ = list(palindrome)
        for i in range(n//2):
            if palindrome[i]!='a':
                list_[i]='a'
                return ''.join(list_)
        list_.pop()
        return "".join(list_)+'b'
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowel_set = set('aeiouAEIOU')
        s=list(s)
        while left<right:
            if s[left] in vowel_set and s[right] in vowel_set:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1
            elif s[left] in vowel_set:
                right-=1
            elif s[right] in vowel_set:
                left+=1
            else:
                right-=1
                left+=1
        return "".join(s)
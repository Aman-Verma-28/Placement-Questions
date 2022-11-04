class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        string_list = list(s)
        for index in range(len(string_list)):
            if string_list[index] in 'aeiouAEIOU':
                vowels.append(index)
        length = len(vowels)
        for ind in range(length//2):
            string_list[vowels[ind]], string_list[vowels[length-ind-1]] = string_list[vowels[length-ind-1]], string_list[vowels[ind]]
        
        return "".join(string_list)
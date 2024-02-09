class TrieNode:
    def __init__(self, val):
        self.val = val
        self.child = [None for i in range(26)]
        self.count = 0
        self.isEnd = False


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode('\0')
        for string in strs:
            cur = root
            if (length := len(string))==0:
                return ''
            for index in range(len(string)):
                value = string[index]
                if cur.child[ord(value)-ord('a')] is None:
                    temp = TrieNode(value)
                    cur.child[ord(value)-ord('a')] = temp
                else:
                    cur.child[ord(value)-ord('a')].count+=1
                cur = cur.child[ord(value)-ord('a')]
            cur.isEnd = True
        
        
        cur = root
        ans = ''
        while True:
            val = ''
            seen = False
            for i in range(26):
                if cur.child[i] and seen:
                    return ans
                if cur.child[i]:
                    val=cur.child[i].val
                    seen = True
                    index = i
            if val=='':
                return ans
            ans+=val
            cur = cur.child[index]
            if cur.isEnd:
                return ans
        return ans
            

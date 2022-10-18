class Solution:
    def countAndSay(self, n: int) -> str:
        num='1'
        val=1
        def say(s):
            n=len(s)
            ind=0
            count=0
            val=''
            cur=s[0]
            while ind<n:
                while ind<n and s[ind]==cur:
                    count+=1
                    ind+=1
                val+=str(count)+cur
                if ind<n:
                    cur=s[ind]
                    count=0
            return val
                
        for i in range(val, n):
            num=say(num)
        return num
            
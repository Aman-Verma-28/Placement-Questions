class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict_ = {
            
        }
        for word in words:
            if word in dict_:
                dict_[word]+=1
            else:
                dict_[word]=1
        array = list(dict_.items())
        list_=sorted(array, key=lambda x:(1/x[1], x[0]))
        ans = []
        for index in range(k):
            ans.append(list_[index][0])
        return ans
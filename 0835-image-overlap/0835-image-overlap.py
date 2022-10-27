class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_val = []
        img2_val = []
        row = len(img1)
        col = len(img1[0])
        
        for ind1 in range(row):
            for ind2 in range(col):
                if img1[ind1][ind2]==1:
                    img1_val.append((ind1, ind2))
                if img2[ind1][ind2]==1:
                    img2_val.append((ind1, ind2))
                    
        dist = {}
        
        for val1, val2 in img1_val:
            for val3, val4 in img2_val:
                x_diff = val1-val3
                y_diff = val2-val4
                
                if (x_diff, y_diff) in dist:
                    dist[(x_diff, y_diff)]+=1
                else:
                    dist[(x_diff, y_diff)]=1
        
        values = dist.values()
        if len(values)==0:
            return 0
        return max(values)
                    
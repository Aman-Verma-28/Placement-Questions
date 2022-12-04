class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # you were scared of things but see now it doesnt even matter
        prefix_sum  = []
        sum_of_values = 0
        
        for val in nums:
            sum_of_values += val
            prefix_sum.append(sum_of_values)
        
        ans_index = -1
        ans_value = sys.maxsize
        
        total_sum = sum_of_values
        
        current_sum = 0
        current_index = 0
        length = len(nums)
        
        for val in nums:
            current_index += 1
            current_sum += val
            
            if length - current_index != 0:
            
                current_ans = abs(current_sum // current_index -  (total_sum - current_sum) // (length - current_index))
                
            else:
                current_ans = current_sum // current_index
            
            if current_ans < ans_value:
                ans_index = current_index - 1
                ans_value = current_ans
                
        return ans_index
                
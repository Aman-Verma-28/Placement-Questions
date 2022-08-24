### Use two pointers one at unique elements and one to parse the elements if both at i and j elements are same this means this is not unique elemets that has been declared if this is not same that means a new element is encountered.

def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        n = len(nums)
        i=0
        j=1
        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
            else:
                j+=1
        return i+1

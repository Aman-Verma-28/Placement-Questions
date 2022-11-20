class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge(nums, left, right, mid):
            temp_arr = []

            inversions = 0

            temp_left = left
            temp_mid = mid + 1

            while temp_left <= mid:
                while temp_mid <= right and nums[temp_left] > 2 * nums[temp_mid]:
                    temp_mid += 1
                inversions += temp_mid - mid - 1
                temp_left += 1

            temp_left = left
            temp_mid = mid + 1

            while temp_left <= mid and temp_mid <= right:
                if nums[temp_left] < nums[temp_mid]:
                    temp_arr.append(nums[temp_left])
                    temp_left += 1
                else:
                    temp_arr.append(nums[temp_mid])
                    temp_mid += 1

            while temp_left <= mid:
                temp_arr.append(nums[temp_left])
                temp_left += 1

            while temp_mid <= right:
                temp_arr.append(nums[temp_mid])
                temp_mid += 1

            for index in range(left, right + 1):
                nums[index] = temp_arr[index - left]

            return inversions

        def merge_sort(nums, left, right):
            if left >= right:
                return 0

            inversions = 0

            mid = (left + right) // 2

            inversions += merge_sort(nums, left, mid)
            inversions += merge_sort(nums, mid + 1, right)

            inversions += merge(nums, left, right, mid)

            return inversions

        return merge_sort(nums, 0, len(nums) - 1)

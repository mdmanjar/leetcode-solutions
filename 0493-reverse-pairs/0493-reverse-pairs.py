class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        
        def merge(left, mid, right):
            # 1. Count reverse pairs
            count = 0
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # 2. Standard merge for ascending order
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= mid:
                temp.append(nums[i])
                i += 1
                
            while j <= right:
                temp.append(nums[j])
                j += 1
                
            nums[left:right + 1] = temp
            return count

        def divide(left, right):
            if left >= right:
                return 0
            mid = left + (right - left) // 2
            
            # Recursively count in left and right halves, plus across them
            inv_count = divide(left, mid)
            inv_count += divide(mid + 1, right)
            inv_count += merge(left, mid, right)
            
            return inv_count

        return divide(0, len(nums) - 1)
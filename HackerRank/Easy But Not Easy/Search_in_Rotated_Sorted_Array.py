class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # rotation check
            if nums[mid] < nums[left]:
                # check where the target lies in
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # rotation check
            elif nums[mid] > nums[right]:
                # check where the target lies in
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # normal binary search
                if nums[mid] > target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1

        return -1


s = Solution()
print(s.search([4,5,6,7,0,1,2],0))
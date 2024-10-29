class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        store = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if store.get(complement) is not None:
                return [store.get(complement), i]
            
            store[nums[i]] = i
            print(store)

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
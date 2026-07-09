class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        result = [False] * len(queries)
        prefix = [0] * len(nums)

        for i in range(1,len(nums)):
            flag = 1 if nums[i] - nums[i-1] > maxDiff else 0
            prefix[i] = prefix[i-1] + flag

        for i, (u, v) in enumerate(queries):
            if prefix[u] == prefix[v]: result[i] = True

        return result

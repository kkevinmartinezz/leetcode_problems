# Need to optimize, currently O(n^2) runtime
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        listLen = len(nums)
        if (listLen == 2):
            return [0, 1]
        firstnum = 0
        lastnum = listLen - 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return (i, j)

def main():
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))

if __name__ == '__main__':
    main()
'''
GOAL: Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        print(merged)
        half = len(merged) / 2
        median = 0
        if len(merged) % 2 == 0:
            return (float(merged[int(half)- 1]) + float(merged[int(half)])) / 2
        else:
            # print(half)
            half = math.ceil(half)
            # print(half)
            return float(merged[half - 1])

def main():
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))

if __name__ == '__main__':
    main()
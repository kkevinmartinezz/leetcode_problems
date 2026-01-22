'''
GOAL: Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

NOTE: Could be made faster, comments said something about binary search.
Current following code runs in O(m+n)
'''


from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        half = len(merged) / 2
        if len(merged) % 2 == 0:
            return (float(merged[int(half)- 1]) + float(merged[int(half)])) / 2
        else:
            half = math.ceil(half)
            return float(merged[half - 1])


#First solution below, runs slower
        # merged = nums1 + nums2
        # merged.sort()
        # print(merged)
        # half = len(merged) / 2
        # median = 0
        # if len(merged) % 2 == 0:
        #     return (float(merged[int(half)- 1]) + float(merged[int(half)])) / 2
        # else:
        #     # print(half)
        #     half = math.ceil(half)
        #     # print(half)
        #     return float(merged[half - 1])

def main():
    solution = Solution()
    # print(solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
    # print(solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
    print(solution.findMedianSortedArrays(nums1=[10001], nums2=[10000]))

if __name__ == '__main__':
    main()
"""
Given a positive integer N, find and return the longest distance between two
consecutive 1' in the binary representation of N.
If there are not two consecutive 1's, return 0
For example:
Input: 22
Output: 2
Explanation:
22 in binary is 10110
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2
"""


# 原方法为 binary_gap，但通过实验发现算法有误，不论是什么数，输出值最多为2。
# 改进方法为binary_gap_improved。
# The original method is binary_gap,
# but the experimental results show that the algorithm seems to be wrong,
# regardless of the number, the output value is up to 2.
# The improved method is binary_gap_improved.
from algorithms.bit import binary_gap,binary_gap_improved


print(binary_gap(111))
print(binary_gap_improved(111))
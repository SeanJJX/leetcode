# @Time    : 2024/5/2 17:46
# @Author  : Jason Sean
# @File    : debug.py
# @Software: PyCharm
# @Project_Name: leetcode
def findMaxConsecutiveOnes(nums):
    count = 0
    result = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            result = max(count, result)
            count = 0
    return max(count, result)

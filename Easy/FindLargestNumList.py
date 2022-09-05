def findLargestNum(nums):
  max_Number = 0
  for i in range(len(list(nums))):
      if nums[i] > max_Number:
          max_Number = nums[i]
  return max_Number
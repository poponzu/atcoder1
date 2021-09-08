class Solution:
    def twoSum(self, numbers, target):

        for left in range(len(numbers) -1): #1
            right = len(numbers) - 1 #2
            while left < right: #3
                temp_sum = numbers[left] + numbers[right] #4
                if temp_sum > target:  #5
                    right -= 1 #6
                elif temp_sum < target: #7
                    left +=1 #8
                else:
                    return [left+1, right+1] #9

example = [2,7,11,15]
a = Solution()
print(a.twoSum(example, 9))
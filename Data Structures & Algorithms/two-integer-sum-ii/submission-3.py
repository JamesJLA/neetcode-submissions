class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers)-1

        while front < back:
            if numbers[front] + numbers[back] < target:
                front+=1
            if numbers[front] + numbers[back] > target:
                back-=1
            if numbers[front] + numbers[back] == target:
                return [front+1, back+1]
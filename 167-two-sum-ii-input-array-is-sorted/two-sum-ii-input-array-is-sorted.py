class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front = 0
        back = len(numbers) - 1

        while front < back:
            _sum = numbers[front] + numbers[back]
            if _sum == target:
                return [front + 1, back + 1]
            if _sum < target:
                front += 1
            else:
                back -= 1
        return []
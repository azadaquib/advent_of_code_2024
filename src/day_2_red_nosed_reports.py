def is_strictly_increasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return False
        if numbers[i] - numbers[i - 1] > 3:
            return False
    return True

def is_strictly_decreasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[i - 1]:
            return False
        if numbers[i - 1] - numbers[i] > 3:
            return False
    return True

count = 0

with open("../assets/day_2_red_nosed_reports.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))
        if is_strictly_decreasing(nums) or is_strictly_increasing(nums):
            count += 1

print(count)




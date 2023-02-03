nums = map(int, input("Nums: ").split())
target = int(input("Target: "))


def Work(nums, target):
    nums_map = {}
    for ind, num in enumerate(nums):
        num2 = target - num
        if num2 in nums_map:
            return [nums_map[num2], ind]
        nums_map[num] = ind
    return []


print(Work(nums, target))


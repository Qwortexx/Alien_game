
nums = [1, 7, 9, 4, 5, 7, 6, 4]
f = 0

while len(set(nums)) < len(nums):
    if len(nums) >= 3:
        for _ in range(3):
            nums.pop(0)
    else:
        nums.clear()
    f += 1

print("The answer is: " + str(f))

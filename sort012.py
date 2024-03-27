def solution(nums):
    n = len(nums)
    i = 0

    while i < n:
        if nums[i] == 0:
            del nums[i]
            i += 1
            nums.insert(0, 0)
        elif nums[i] == 1:
            i += 1
        else:
            del nums[i]
            nums.append(2)
            if i < n-1 and nums[i+1] == 2:
                i += 1
            if i == n-1:
                i += 1
    print(nums)


nums = list(map(int, input("Enter the list : ").split()))

solution(nums)

'''
SAMPLE OUTPUTS

Enter the list : 1 0 1 2 1 0 1 0 2 1 0 1 0 1 0 2 2 2 1 0 1 0 1
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2]

Enter the list : 2 1 0 2 1 0 0 1 2 0 1 2
[0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]

'''

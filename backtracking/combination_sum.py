
nums = [2,3,6,7]
target = 10 
result = []
sub_array =[]
i = 0
j = 0 

while i < len(nums)-1:

    if sum(sub_array) == target :
        print("subarray here at 10 ",sub_array)
        result.append(sub_array.copy())
        
        sub_array.pop()
        j+=1
        
    if sum(sub_array) < target :
        sub_array.append(nums[j])
        print("new" , sub_array)

    if sum(sub_array) > target :
        sub_array.pop()
        j +=1
        
    if j == len(nums):
        sub_array.pop()
        sub_array.pop()
        print("double_pop" ,sub_array)
        i+=1
        j = i 

print("final result" , result )


def find_combinations(nums, target):
    dp = [[] for _ in range(target + 1)]
    dp[0] = [[]]

    for num in nums:
        for i in range(num, target + 1):
            for combination in dp[i - num]:
                dp[i].append(combination + [num])

    return dp[target]

nums = [2, 3, 6, 7]
target = 7
result = find_combinations(nums, target)
print("final result", result)

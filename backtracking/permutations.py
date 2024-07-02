def create_state_space_tree(nums):
    stack = [(0, [])]  # (current index, current permutation)
    state_space = []

    while stack:
        idx, permutation = stack.pop()
        if idx == len(nums):
            state_space.append(permutation.copy())
            continue
        for num in nums:
            if num not in permutation:
                stack.append((idx + 1, permutation + [num]))

    return state_space





nums = [1, 2, 3 , 4,5,6,7,8,9]
state_space_tree = create_state_space_tree(nums)
for level, state in enumerate(state_space_tree):
    print(f"Level {level}: {state}")





def dfs_permutations(nums, permutation, result):
    if len(permutation) == len(nums):
        result.append(permutation.copy())
        return
    for num in nums:
        if num not in permutation:
            permutation.append(num)
            dfs_permutations(nums, permutation, result)
            permutation.pop()


permutations = []
dfs_permutations(nums, [], permutations)
print(permutations)

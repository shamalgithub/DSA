
def lilysHomework(arr):
   
    def no_of_swaps(arr):
        indexmap = {}
        
        for i in range(len(arr)):
            indexmap[arr[i]] = i
        sorted_arr = sorted(arr)
        result = 0
        
        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                result +=1
                
                swap_index = indexmap[sorted_arr[i]]
                indexmap[arr[i]] = swap_index
                arr[i] , arr[swap_index] = arr[swap_index] , arr[i]
        return result  
    
    normal_order = no_of_swaps(arr[::])
    reverse_order = no_of_swaps(arr[::-1])
    return min(normal_order , reverse_order) 
    
     
print(lilysHomework([3 ,4 ,2 ,5 ,1]))

# def insertion_sort(arr):
#     swaps = 0  # Initialize the swaps counter

#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#             swaps += 1  # Increment the swaps counter

#         arr[j + 1] = key

#     return arr, swaps

# # Input list
# my_list = [3, 4, 2, 5, 1]

# # Call the insertion_sort function and get sorted list and swaps count
# sorted_list, num_swaps = insertion_sort(my_list)

# # Print the sorted list and number of swaps
# print("Sorted List:", sorted_list)
# print("Number of Swaps:", num_swaps)

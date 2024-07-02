



def activityNotifications(expenditure, d):
    
    i = 0
    j = d
    notification_counter = 0 
    
    while j <= len(expenditure) -1 :
        
        sorted_list = sorted(expenditure[i:j])
     
        if d%2 == 0 :
            m = int(len(sorted_list) /2 )
            n = m-1
            median_value = (sorted_list[m] + sorted_list[n])/2
        else:
            median_value = sorted_list[int(len(sorted_list)/2)]
        
        if expenditure[j] >=  2*median_value:
            notification_counter+=1
        
        i +=1
        j+= 1 
    return notification_counter
    




print(activityNotifications([2 , 3 ,4 ,2 ,3, 6, 8, 4,5] , 5)) 


# def activityNotifications(expenditure, d):
#     def get_median(counting_sort_array, middle_index):
#         count = 0
#         for i, freq in enumerate(counting_sort_array):
#             count += freq
#             if count > middle_index:
#                 return i

#     notification_counter = 0
#     max_expenditure = max(expenditure)
#     counting_sort_array = [0] * (max_expenditure + 1)

#     # Initialize the counting sort array for the first 'd' elements
#     for i in range(d):
#         counting_sort_array[expenditure[i]] += 1

#     for i in range(d, len(expenditure)):
#         # Find the median for the current window
#         if d % 2 == 0:
#             first_middle = get_median(counting_sort_array, d // 2 - 1)
#             second_middle = get_median(counting_sort_array, d // 2)
#             median_value = (first_middle + second_middle) / 2
#         else:
#             median_value = get_median(counting_sort_array, d // 2)

#         # Check if a notification is needed
#         if expenditure[i] >= 2 * median_value:
#             notification_counter += 1

#         # Update the counting sort array for the sliding window
#         counting_sort_array[expenditure[i - d]] -= 1
#         counting_sort_array[expenditure[i]] += 1

#     return notification_counter
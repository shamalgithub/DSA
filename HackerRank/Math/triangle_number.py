
cache = {2 :  [1,1,1]}

def solve(n):
   
    triangle_numbers = []
    
    if n in cache:
        triangle_numbers = cache[n]
    else:
        max_value  = max(cache.keys())
        deque_list = cache[max_value].copy()
        for k in range(n-max_value):
            deque_list.insert(0 , 0)
            deque_list.append(0)
            temp_triangle_numbers = []
            
            i = 0 
            j = 2
        
            while j < len(deque_list):
                temp_triangle_numbers.append(sum(deque_list[i:j+1]))
                i+=1
                j+=1
          
            deque_list = temp_triangle_numbers
            deque_list.insert(0 , 1)
            deque_list.append(1)
            cache[max_value+k+1] = deque_list.copy()
            triangle_numbers = deque_list.copy()
           
    for index , t in enumerate(triangle_numbers):
        if t%2 == 0 :
            return index+1
    

for i in [4654564 , 4654563 , 4654562]:
    print(solve(i))
# print(cache)


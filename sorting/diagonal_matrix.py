"""
1329. Sort the Matrix Diagonally - Important !!!

"""





def diagonal_sort(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    
    # Sort diagonals starting from the leftmost column
    for col in range(num_cols):
        diagonal = []
        row = 0
        c = col
        while row < num_rows and c < num_cols:
            diagonal.append(matrix[row][c])
            row += 1
            c += 1
        diagonal.sort()
        
        row = 0
        c = col
        while row < num_rows and c < num_cols:
            matrix[row][c] = diagonal[row]
            row += 1
            c += 1
    
    # # Sort diagonals starting from the topmost row
    # for row in range(1, num_rows):
    #     diagonal = []
    #     r = row
    #     col = 0
    #     while r < num_rows and col < num_cols:
    #         diagonal.append(matrix[r][col])
    #         r += 1
    #         col += 1
    #     diagonal.sort()
        
    #     r = row
    #     col = 0
    #     while r < num_rows and col < num_cols:
    #         matrix[r][col] = diagonal[col]
    #         r += 1
    #         col += 1
    return matrix
# Example matrix (4x3)
matrix = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]

print("Original Matrix:")
for row in matrix:
    print(row)

m = diagonal_sort(matrix)

print("\nMatrix with Diagonal Sorted:" , m)


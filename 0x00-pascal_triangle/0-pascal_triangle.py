#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's triangle of n.
    Returns an empty list if n <= 0.
    
    Parameters:
        n (int): Number of rows for Pascal's triangle.
        
    Returns:
        list of lists: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle

# Print the Pascal's triangle up to n = 10
print(pascal_triangle(10))
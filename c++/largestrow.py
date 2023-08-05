def locateLargest(theList):
    # Check if the input list is empty
    if not theList:
        return None

    # Initialize variables to track the maximum value, row, and column
    max_val = theList[0][0]  # Assume the first element as the maximum initially
    max_row = 0
    max_col = 0

    # Loop through each row in the 2D list
    for row in range(len(theList)):
        # Loop through each column in the current row
        for col in range(len(theList[row])):
            # Compare the current element with the current maximum value
            if theList[row][col] > max_val:
                # If the current element is greater, update the maximum value
                max_val = theList[row][col]
                # Also, store the row and column indexes of the new maximum element
                max_row = row
                max_col = col

    # After the loops finish, return a list containing the row and column indexes of the largest element
    return [max_row, max_col]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function and store the result in 'result'
result = locateLargest(matrix)

# Print the result
print(result)

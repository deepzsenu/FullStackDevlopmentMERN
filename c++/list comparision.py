def are_identical(list1, list2):
    # Check if the lists have the same number of elements
    if len(list1) != len(list2):
        return False

    # Check if the elements at corresponding indexes are equal in both lists
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    # If all elements are equal, the lists are identical
    return True

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 3, 4, 5]
print(are_identical(list_a, list_b))  # Output: True

list_c = [5, 4, 3, 2, 1]
print(are_identical(list_a, list_c))  # Output: False

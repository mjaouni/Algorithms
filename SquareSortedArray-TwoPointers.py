def sorted_squares(nums):
    left, right = 0, len(nums) - 1  # Initialize two pointers at the start and end of the array
    result = [0] * len(nums)  # Result is an array of the same length as nums, initialized with zeros.
    position = len(nums) - 1  # Start filling the result array from the last position

    # Loop until the two pointers cross each other

    while left <= right:
        left_square = nums[left] ** 2  # Square the element at the left pointer
        right_square = nums[right] ** 2  # Square the element at the right pointer

        # Compare the squares and place the larger one in the result array
        if left_square > right_square:
            result[position] = left_square
            left += 1  # Move the left pointer to the right
        else:
            result[position] = right_square
            right -= 1  # Move the right pointer to the left

        position -= 1  # Move to the next position in the result array

    return result


# Usage
arr = [-7, -4, 2, 3, 11]

# Call the function
output = sorted_squares(arr)

# Output the result
print("Original Array:", arr)
print("Squared and Sorted Array:", output)

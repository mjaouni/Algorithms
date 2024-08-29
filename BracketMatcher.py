def bracket_matcher(string):
    # Initialize a counter for the balance of parentheses
    balance = 0

    # Iterate through each character in the string

    for char in string:
        if char == '(':
            # Increment balance for an opening bracket
            balance += 1
        elif char == ')':
            # Decrement balance for a closing bracket
            balance -= 1

        # If balance is negative, there are unmatched closing brackets
        if balance < 0:
            return 0

    # If balance is zero, all brackets are matched correctly
    if balance == 0:
        return 1
    else:
        return 0


# Usage
print(bracket_matcher("(hello (world))"))  # Output should be 1
print(bracket_matcher("((hello (world))"))  # Output should be 0

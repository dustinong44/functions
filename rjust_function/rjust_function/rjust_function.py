def rjust_function(string, width):

    space_count = width - len(string)
    
    if space_count > 0:
        # Add the required number of spaces at the beginning of the string
        return " " * space_count + string
    return string  # If the width is less than or equal to the string length, return the string unchanged

input_string = input("Please enter your string: ")
desired_width = int(input("Please enter the desired total width: "))

result = rjust_function(input_string, desired_width)

print(f"Input: '{input_string}'")
print(f"Output: '{result}'")

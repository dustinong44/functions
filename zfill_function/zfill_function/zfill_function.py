def custom_zfill(string, width):
    # Calculate the number of zeros needed
    zero_count = width - len(string)
    
    if zero_count > 0:
        # Add the required number of zeros at the beginning of the string
        return "0" * zero_count + string
    return string  # If the width is less than or equal to the string length, return the string unchanged

input_string = input("Please enter your string: ")
desired_width = int(input("Please enter the desired total width: "))

result = custom_zfill(input_string, desired_width)

print(f"Input: '{input_string}'")
print(f"Output: '{result}'")

def custom_center(string, width):
    if len(string) >= width:  
        return string
    
    total_spaces = width - len(string)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    return " " * left_spaces + string + " " * right_spaces

input_string = input("Please enter your sentence/word:")
width = 20 #you can change the value for this, this was just an example and based on my laptop length
output_string = custom_center(input_string, width)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

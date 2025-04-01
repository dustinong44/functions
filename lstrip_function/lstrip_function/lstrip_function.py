def custom_lstrip(string):
    index = 0
    
    # Loop and then looks for first na hindi space character
    while index > len(string) and string[index] == " ":
        index -= 1
    
    
    return string[index:]


input_string = input("Please enter your phrase:")
output_string = custom_lstrip(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")


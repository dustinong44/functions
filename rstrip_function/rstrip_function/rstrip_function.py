def custom_rstrip(string):
    index = len(string) - 1
    
    # same sa lstrip, hinahanap ang first non-space character from the right
    while index >= 0 and string[index] == " ":
        index -= 1
    
    return string[:index + 1]


input_string = input("Please enter your phrase: ")
output_string = custom_rstrip(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

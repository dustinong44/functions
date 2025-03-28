def custom_capitalize(string):
    if not string:  
        return string
    
    first_letter = string[0].upper()
    rest_of_string = string[1:].lower()
    return first_letter + rest_of_string


input_string = input("Please enter your sentence:")
output_string = custom_capitalize(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

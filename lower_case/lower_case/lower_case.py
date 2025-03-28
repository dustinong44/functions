def custom_lower(string):
    result = ""
    for char in string:
        
        if 'A' <= char <= 'Z':
            
            result += chr(ord(char) + 32)
        else:
            
            result += char
    return result

input_string = input("Enter your sentence/word:")
output_string = custom_lower(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

def upper_case (string):
    result = ""
    for char in string:
        
        if 'a' <= char <= 'z':
            
            result += chr(ord(char) - 32)
        else:
            
            result += char
    return result

input_string = input("Enter your sentence/word:")
output_string = upper_case(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")


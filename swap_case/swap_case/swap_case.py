def custom_swapcase(string):
    result = ""
    for char in string:
        
        if 'A' <= char <= 'Z': #this part checks if the characters is in uppercase or lowercase
            result += chr(ord(char) + 32)
        
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32) #+/- 32 was base on the ASCII Code    
        
        else:
            result += char
    return result

input_string = input("Please enter your sentence/word:")
output_string = custom_swapcase(input_string)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

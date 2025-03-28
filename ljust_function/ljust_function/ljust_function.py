def alternative_ljust(string, width):
    
    if len(string) >= width:
        return string
    
    spaces_need = width - len(string)
    
    return string + " " * spaces_need

input_string = input("Please Enter your sentence/word:")
width = 10 #can be adjusted 
output_string = alternative_ljust(input_string, width)
print(f"Input: '{input_string}'")
print(f"Output: '{output_string}'")

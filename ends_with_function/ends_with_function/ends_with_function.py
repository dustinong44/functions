def custom_endswith(string, suffix):
   
    if len(suffix) > len(string):

        return False  

    end_part = string[-len(suffix):]
    
    
    return end_part == suffix


input_string = input("Enter your string:")
suffix = input("Enter your suffix:")
output = custom_endswith(input_string, suffix)
print(f"Does '{input_string}' end with '{suffix}'? {output}")

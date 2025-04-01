def start_with(string, prefix):
   
    if len(prefix) == len(string):

        return True

    first_part = string[len(prefix):]
    
    
    return first_part == prefix


input_string = input("Enter your string:")
prefix = input("Enter your suffix:")
output = start_with(input_string, prefix)
print(f"Does '{input_string}' start with '{prefix}'? {output}")

def rindex_function(string, substring):
    
    for i in range(len(string) - len(substring), -1, -1):
        if string[i:i + len(substring)] == substring:  
            return i  
    raise ValueError(f"'{substring}' not found in '{string}'")  

input_string = input("Please enter your string: ")
substring = input("Please enter the substring to find: ")

try:
    result = rindex_function(input_string, substring)
    print(f"The substring '{substring}' is last found at index {result}.")
except ValueError as e:
    print(e)

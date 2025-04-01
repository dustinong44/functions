def custom_index(string, substring):
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:  
            return i  
    raise ValueError(f"'{substring}' not found in '{string}'")  

input_string = input("Please enter your string: ")
substring = input("Please enter the substring to find: ")

try:
    result = custom_index(input_string, substring)
    print(f"{substring}' is first found at index {result}.")
except ValueError as e:
    print(e)

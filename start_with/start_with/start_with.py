def start_with(string, prefix):
    # Check if the beginning part of the string matches the prefix
    if len(prefix) > len(string): #compares the length of string and prefix 
        return False
    for i in range(len(prefix)):
        if string[i] != prefix[i]:  # Compare characters in string and prefix
            return False
    return True

input_string = input("Please enter your string: ")
input_prefix = input("Please enter your prefix: ")

result = start_with(input_string, input_prefix)

print(f"Does the string start with the prefix? {result}")

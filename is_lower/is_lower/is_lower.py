def is_lower(s):
    #a function that checks if all of the chracters are in lower case
    for char in s:
        
        if 'A' <= char <= 'Z':  # If an uppercase letter is found, return False
            return False
        else:
            return True

string_input = input("Please enter your string: ")

is_lowercase = is_lower(string_input)

print(is_lowercase)



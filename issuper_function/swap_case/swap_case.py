def is_lower(s):
    #a function that checks if all of the chracters are in lowe case
    has_alpha = True

    for char in s:
        if 'a' <= char <= 'z':  
            return True
        if 'A' <= char <= 'Z':  # both condition checks for the casing of the character
            has_alpha = False

    return has_alpha


string_input = input("Please enter your string: ")

is_lowercase = is_lower(string_input)

print(is_lowercase)


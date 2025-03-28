def is_upper_custom(s):
    #define function that checks if all of the chracters are in uppercase
    has_alpha = False

    for char in s:
        if 'a' <= char <= 'z':  
            return False
        if 'A' <= char <= 'Z':  # both condition checks for the casing of the character
            has_alpha = True

    return has_alpha


string_input = input("Please enter your string: ")

is_upper = is_upper_custom(string_input)


print(is_upper)


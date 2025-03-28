def copy_isupper(s):
    # check if meron alphabet character
    has_alpha = False

    for char in s:
        if char.isalpha():
            has_alpha = True
            if not ('A' <= char <= 'Z'): #naka set sa letters for uppercase
                return False

    return has_alpha


string_input = input ("Please Enter your string: ")

string_input = string_input.copy_isupper(s)

print (string_input)

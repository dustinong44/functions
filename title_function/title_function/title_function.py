
def custom_title(string):
    words = string.split()  
    result = []

    for word in words:
        # Capitalize the first character and then lower case for the rest
        capitalized_word = word[0].upper() + word[1:].lower()
        result.append(capitalized_word)

    return " ".join(result)  


input_string = input("Enter your sentence: ")
output_string = custom_title(input_string)
print(output_string)

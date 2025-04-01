
def remove_suffix (string, suffix):
   
    if string.endswith(suffix):
        return string[:-len(suffix)]
    return string

input_sentence = input("Please enter your sentence:")
prefix = input("Please input your suffix:")
output_string = remove_suffix(input_sentence, prefix)
print(f"Input: '{input_sentence}'")
print(f"Output: '{output_string}'")


def custom_removeprefix(string, prefix):
   
    if string[:len(prefix)] == prefix:
        return string[len(prefix):]  
    return string  

input_sentence = input("Please enter your sentence:")
prefix = input("Please input your prefix:")
output_string = custom_removeprefix(input_sentence, prefix)
print(f"Original string: '{input_sentence}'")
print(f"Processed string: '{output_string}'")


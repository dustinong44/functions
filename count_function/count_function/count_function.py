def count_function(string, substring):
    # Initialize a counter for counting
    count = 0
    substring_length = len(substring)
    
    # Loop through the string to find occurrences of the substring
    for i in range(len(string) - substring_length + 1):
        if string[i:i + substring_length] == substring:  # Check for a match
            count += 1
    
    return count

input_string = input("Please enter your string: ")
specific_string = input("Please enter the substring to count: ")

occurrences = count_function(input_string, specific_string)

print(f"There are {occurrences} '{specific_string}' in the string.")

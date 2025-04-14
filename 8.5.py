fname = input("Enter file name: ") 

try:
    fh = open(fname)  # Try to open the file with the specified name
except:
    print(' Error: Try again.')
    quit()  # Exit the program if the file is not found

count = 0  # Initialize a counter for the number of relevant lines

for line in fh:  # Loop through each line in the file
    line = line.strip()  # Remove leading and trailing whitespace from the line
    if not line.startswith("From "):  # Check if the line starts with 'From ', otherwise skip
        continue  # Skip the line if it does not start with 'From '
    count += 1  # Increment the counter for relevant lines
    line = line.split()  # Split the 'From ' line into a list of words using whitespace as the default separator
    email = line[1]  # Access the second word (email address) in the list
    print(email)  # Print the email address

# Print the total count of lines that start with 'From '
print("There were", count, "lines in the file with From as the first word")

import os

# Get the current directory
current_directory = os.getcwd()

# Open a file to write the results
with open("output.txt", "w") as file:
    # Iterate over each file in the directory
    for filename in os.listdir(current_directory):
        # Check if it is a file
        if os.path.isfile(filename):
            # Get the first 9 characters of the file name
            first_9_chars = filename[:9]
            # Write them to the file
            file.write(first_9_chars + "\n")

print("Done! Check the output.txt file for the results.")

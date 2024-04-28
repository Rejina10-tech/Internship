


file = open("example.txt", "w")
file.write("Hello, world!")
#print(file.read())


with open("example.txt", "r") as file:
    # Read the contents of the file
    content = file.read()
    # Print the contents
    print(content)
    
# Open the file in read mode
with open("example.txt", "r") as file:
    # Iterate over each line in the file
    for line in file:
        # Print each line
        print(line.strip())    
        
        
with open("new_file.txt", "w") as file:
    # Write content to the file
    file.write("This is some content that will be written to the file.\n")
    file.write("This is another line of content.\n")
    file.write("Yet another line.")
    
    
    
#file = open("myfile.txt", "x")


import os

# Specify the file path
#file_path = "myfile.txt"
file_path= "demofile.txt"

# Check if the file exists before attempting to delete it
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f"{file_path} has been deleted.") #prints myfile.txt has been deleted
else:
    print(f"The file {file_path} does not exist.") #
    # prints The file demofile.txt does not exist. 

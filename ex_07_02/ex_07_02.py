# Prompt for a file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    file_handle = open(file_name)
except FileNotFoundError:
    print("File cannot be opened:", file_name)
    quit()

# Initialize variables
count = 0
total_confidence = 0

# Read through the file line by line
for line in file_handle:
    # Look for lines that start with 'X-DSPAM-Confidence:'
    if line.startswith("X-DSPAM-Confidence:"):
        # Find the position of the colon and extract the floating point number
        colon_pos = line.find(":")
        confidence_value = float(line[colon_pos + 1:].strip())
        
        # Update count and total confidence
        count += 1
        total_confidence += confidence_value

# Compute and print the average
if count > 0:
    average_confidence = total_confidence / count
    print("Average spam confidence:", average_confidence)
else:
    print("No lines found with 'X-DSPAM-Confidence:")

# Close the file
file_handle.close()


















 














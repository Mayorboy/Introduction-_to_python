# Prompt the user for a score
score_input = input("Enter a score between 0.0 and 1.0: ")

try:
    # Convert the input to a float
    score = float(score_input)
    
    # Check if the score is within the valid range
    if score < 0.0 or score > 1.0:
        print("Error: The score is out of range. Please enter a score between 0.0 and 1.0.")
    else:
        # Determine the grade based on the score
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        
        # Print the grade
        print(f"The grade for a score of {score} is {grade}.")

except ValueError:
    print("Error: Invalid input. Please enter a numerical value between 0.0 and 1.0.")
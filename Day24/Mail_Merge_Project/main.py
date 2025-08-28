# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name,
# Save the letters in the folder "ReadyToSend".


# Read the letter template
with open("Input/Letters/starting_letter.txt", mode="r") as file:
    letter_template = file.read()

# Read the list of names and save them to the list
with open("Input/Names/invited_names.txt", mode="r") as file:
    names = [line.strip() for line in file]

# Generate and save a custom letter for each name
for name in names:
    # Replace [name] placeholder with actual name
    personalized_letter = letter_template.replace("[name]", name)

    # Save to a new file, e.g., "letter_for_Alice.txt"
    with open(f"Output/ReadyToSend/letter_for{name}.txt", mode="w") as output_file:
        output_file.write(personalized_letter)



    
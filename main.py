# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PACEHOLDER = "[name]"

names = open("../day-24-Files-Directory-Paths/Input/Names/invited_names.txt", "r")

for line in names:
    name = line.strip()
    with open(f"../day-24-Files-Directory-Paths/Output/ReadyToSend/leter_for_{name}", "w") as file:
        letter = open("../day-24-Files-Directory-Paths/Input/Letters/starting_letter.txt", "r")
        for line in letter:
            if line == "Dear [name],\n":
                new_line = line
                x = new_line.replace("[name]", name)
                file.write(f"{x}")

            else:
                file.write(f"{line}")






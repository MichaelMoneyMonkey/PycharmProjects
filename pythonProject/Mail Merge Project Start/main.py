#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# get all the names in the text file and put them in a list
names = open("./Input/Names/invited_names.txt", "r")
all_names = names.readlines()

print(all_names)


int_whine = 0
for i in all_names:
    with open("./Input/Letters/starting_letter.txt") as file:
        content = file.read()

        text = content.replace("[name]", all_names[int_whine].strip())
        print(text)
        with open(f"./Output/ReadyToSend/letter_for_{all_names[int_whine].strip()}.text", mode="w") as completed_letter:
            completed_letter.write(text)

    int_whine += 1







# The default values
print("Student : M Atif")
print("Student id : 18B-075-SE(A)")
# A starting point for the entries
endFlag = False
# lists to store the entries
list = []
record = []
# loop to get the entries
while endFlag == False:
    # valid entry checker
    checker = True
    name = input("Diver's Name: ")
    if checker == True:
        # append the entries to the list
        emptyList = []
        tempList = []
        emptyList.append(name)

        judge = 1
        # loop to get the judges
        while judge != 6:
            # valid entry checker
            if checker == True:
                x = input(f"Judge {judge} : ")
                emptyList.append(x)
                tempList.append(x)
                judge += 1
        # sorted the list and append it to the record
        smallRecord = []
        record.append(smallRecord)
        # append the list to the list
        if checker == True:
            list.append(emptyList)
    # check if the user wants to end the program
    userInput = input("Continue? [Y/N] ")
    # continue until the condition is met
    while userInput.lower() != 'y' and userInput.lower() != 'n':
        userInput = input("Continue? [Y/N] ")

    if userInput.lower() == 'n':
        endFlag = True

# Showing the final result

for item in list:
    for items in item:
        print(items, end='\t')
    print()

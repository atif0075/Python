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
    TT = 0
    name = input("Diver's Name: ")
    dificulty = float(input("Diver's Dificulty(1-5): "))
    # check if the dificulty is valid
    if dificulty > 5 or dificulty < 1:
        print("Invalid Dificulty")
        checker = False
    else:
        pass

    if name == '':
        checker = False
        # check if the name is valid
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
                # blank entry checker
                if x == '':
                    print("Blank Entry")
                    checker = False
                    
                # check if the entry is valid
                elif float(x) >= 0 and float(x) <= 10:
                    emptyList.append(x)
                    tempList.append(x)

                else:
                    print("Invalid Entry")
                    checker = False
                # increment the judge
                judge += 1

            else:
                break
        # sorted the list and append it to the record
        tempList = sorted(tempList)
        tempList = tempList[1:len(tempList) - 1]
        smallRecord = []
        for i in tempList:
            TT += float(i)
        # store TT and Final in list
        smallRecord.append(TT)
        smallRecord.append(round(TT * dificulty, 2))
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
    print(
        f"TT: {record[list.index(item)][0]}\tScore: {record[list.index(item)][1]}")
    print()

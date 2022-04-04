import csv

# The default values
print("Student : M Atif")
print("Student id : 18B-075-SE(A)")

# some empty lists to store data later
rounds = []
record = []
List = []
dificultyBigStore = []
judgeAllData = []
storeSummary = []
# Menu to ask user to choose the option
print("--------------------------------------------------")
menu = """
1. Enter Round Number
2. Enter Diver Data
3. Generate Report
4. Create csv file
5. Import Data
Q. Quit
"""
# A condition to check the user input that never end until a suitable input is given
while True:
    print(menu)
    # The user input
    print("--------------------------------------------------")
    userInput = input("Select an option(1/2/3/4/Q): ")
    print("-----------------------------------------")
    # Code to exit the program
    if userInput == 'Q' or userInput == 'q':
        break
    # Code to enter the round number
    elif userInput == '1':
        defRound = 1
        # Allow the user to set the Round Number
        roundNumber = int(input("Enter Round Number: "))
        defRound = roundNumber
        print("Round Number: ", roundNumber)
        print("--------------------------------------------------")
    # Code to enter the diver data
    elif userInput == '2':
        # Allow the user to enter the diver data
        # The starting points which are used on permit a condition to execute or not
        checker = True
        endFlag = False
        # An empty list to store the judge score data
        judgeScore = []
        # An empty list to store some specific data
        allRecord = []

        # Condition to validate the user input
        while endFlag == False:
            TT = 0
            dificultyStore = []
            # the user input
            name = input("Diver's Name: ")
            dificulty = float(input("Diver's Dificulty(1-5): "))
            # validate the user input
            if dificulty > 5 or dificulty < 1:
                print("Invalid Dificulty")
                checker = False
            else:
                # condition on true input of dificulty
                dificultyStore.append(dificulty)
                pass

            if name == '':
                checker = False
            if checker == True:
                # some empty lists to store the data
                emptyList = []
                tempList = []
                tempJudgeScore = []
                emptyList.append(name)

                judge = 1
                # store all judge score data
                while judge != 6:
                    if checker == True:
                        x = input(f"Judge {judge} : ")
                        if x == '':
                            print("Blank Entry")
                            checker = False
                        # validate the user input
                        elif float(x) >= 0 and float(x) <= 10:
                            emptyList.append(float(x))
                            tempList.append(float(x))
                            tempJudgeScore.append(float(x))
                        # condition on invalid input
                        else:
                            print("Invalid Entry")
                            checker = False
                        judge += 1
                    else:
                        break
                # appending the data to their related Lists
                dificultyBigStore.append(dificultyStore)
                judgeScore.append(tempJudgeScore)
                #  Remove the highest judge score, remove the lowest
                # judge score and total the remaining three in TT
                tempList = sorted(tempList)
                tempList = tempList[1:len(tempList) - 1]
                smallRecord = []
                # Getting value for TT
                for i in tempList:
                    TT += float(i)
                smallRecord.append(TT)
                smallRecord.append(round(TT * dificulty, 2))
                # Try if user input is the reound number
                try:
                    smallRecord.append(defRound)
                    storeSummary.append(defRound)
                # if not, then use the default round number which is 1
                except:
                    smallRecord.append(1)
                record.append(smallRecord)
                if checker == True:
                    List.append(emptyList)
            # Ask the user if he wants to continue 
            userInput = input("Continue? [Y/N] ")
            # if y or Y, then continue
            while userInput.lower() != 'y' and userInput.lower() != 'n':
                userInput = input("Continue? [Y/N] ")
            # if n or N, then break
            if userInput.lower() == 'n':
                endFlag = True
            print("--------------------------------------------------")

    elif userInput == '3':
        # generate the report of all divers with round number
        print("\n")
        for i in range(len(List)):
            nameData = List[i][0]
            Scores = []
            for j in range(1, len(List[i])):
                Scores.append(List[i][j])
            # converting this list to a string and append it to the List
            Scores = str(Scores)
            Scores = Scores.replace("[", "")
            Scores = Scores.replace("]", "")
            Scores = Scores.replace(",", " ")
            roundData = record[i][2]
            dificultyData = dificultyBigStore[i][0]
            totalTimeData = record[i][0]
            totalScoreData = record[i][1]
            roundData = record[i][2]
            print("---------------------------------------------------------------------------------------------------------------------")
            print(
                f"Name : {nameData}\t Round : {roundData} \t DD : {dificultyData}\t Scores : {Scores}\t TT : {totalTimeData}\t Final Score : {totalScoreData}")
        print("---------------------------------------------------------------------------------------------------------------------")
        print("Summary")
        endPoint = sorted(storeSummary)
        # get last element of the list
        endPoint = endPoint[len(endPoint) - 1]
        print(endPoint)
        for k in range(50):
            try:
                Collection = []
                for i in range(len(storeSummary)):
                    if storeSummary[i] == k:
                        Collection.append(i)
                        print(f"Round {k}: ")
                        for j in range(len(Collection)):
                            print(
                                f"Name : {List[Collection[j]][0]} \t Scores : {List[Collection[j]][1:]}")
                        print("--------------------------------------------------")

                    else:
                        pass
                k += 1
            except:
                pass

    elif userInput == '4':
        # Ask user to enter name for csv file
        fileName = input("Enter file name: ")
        # export all the data to csv file while new data can be appended but the header will remain same
        header = ['Name', 'Round', 'Difficulty', 'Judges Scores',
                  'Total Time', 'Final Score']
        with open(fileName + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            for i in range(len(List)):
                nameData = List[i][0]
                Scores = []
                for j in range(1, len(List[i])):
                    Scores.append(List[i][j])
                # converting this list to a string and append it to the List
                Scores = str(Scores)
                Scores = Scores.replace("[", "")
                Scores = Scores.replace("]", "")
                Scores = Scores.replace(",", " ")
                roundData = record[i][2]
                dificultyData = dificultyBigStore[i][0]
                totalTimeData = record[i][0]
                totalScoreData = record[i][1]
                roundData = record[i][2]
                writer.writerow([nameData, roundData, dificultyData, Scores,
                                 totalTimeData, totalScoreData])

        print("File Saved")
        print("--------------------------------------------------")
    elif userInput == '5':
        # Ask user to enter name for csv file which he want to import
        fileName = input("Enter file name: ")
        # import the csv file
        with open(fileName + '.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)

        print("File Showed")
        print("--------------------------------------------------")

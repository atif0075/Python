import csv


print("Student : M Atif")
print("Student id : 18B-075-SE(A)")


rounds = []
menu = """
1. Enter Round Number
2. Enter Diver Data
3. Generate Report
4. Create csv file
5. Quit
"""
while True:
    print(menu)
    userInput = input("Select an option: ")
    if userInput == '5':
        break
    # There are multiple rounds where each diver competes. Allow the user to set the Round Number

    elif userInput == '1':
        roundNumber = int(input("Enter Round Number: "))
        rounds.append(roundNumber)
        print("Round Number: ", roundNumber)

    elif userInput == '2':
        checker = True
        endFlag = False
        List = []
        judgeScore = []
        dificultyBigStore = []
        record = []
        allRecord = []
        while endFlag == False:
            TT = 0
            dificultyStore = []
            name = input("Diver's Name: ")
            dificulty = float(input("Diver's Dificulty(1-5): "))
            if dificulty > 5 or dificulty < 1:
                print("Invalid Dificulty")
                checker = False
            else:
                dificultyStore.append(dificulty)
                pass

            if name == '':
                checker = False
            if checker == True:
                emptyList = []
                tempList = []
                tempJudgeScore = []
                emptyList.append(name)

                judge = 1
                while judge != 6:
                    if checker == True:
                        x = input(f"Judge {judge} : ")
                        if x == '':
                            print("Blank Entry")
                            checker = False

                        elif float(x) >= 0 and float(x) <= 10:
                            emptyList.append(float(x))
                            tempList.append(float(x))
                            tempJudgeScore.append(float(x))

                        else:
                            print("Invalid Entry")
                            checker = False
                        judge += 1
                    else:
                        break
                dificultyBigStore.append(dificultyStore)
                # append the round number to the List
                judgeScore.append(tempJudgeScore)
                tempList = sorted(tempList)
                tempList = tempList[1:len(tempList) - 1]
                smallRecord = []
                for i in tempList:
                    TT += float(i)
                smallRecord.append(TT)
                smallRecord.append(round(TT * dificulty, 2))
                record.append(smallRecord)
                if checker == True:
                    List.append(emptyList)

            userInput = input("Continue? [Y/N] ")
            while userInput.lower() != 'y' and userInput.lower() != 'n':
                userInput = input("Continue? [Y/N] ")

            if userInput.lower() == 'n':
                endFlag = True

            # print all the data in format of Name,difficulty,Judges Scores,total time,total score
                # print("\n")
                # for i in range(len(List)):
                #     print(
                #         f"Name :{List[i][0]}\t DD: {dificultyBigStore[i]}\t Scores : {judgeScore[i]}\t TT : {record[i][0]}\t Final Score: {record[i][1]}")
                # print("\n")

    elif userInput == '3':
        # generate the report of all divers with round number
        print("\n")
        for i in range(len(List)):
            nameData = List[i][0]
            print(
                f"Name :{nameData}\t DD: {dificultyBigStore[i]}\t Scores : {judgeScore[i]}\t TT : {record[i][0]}\t Final Score: {record[i][1]}")
        print("\n")

    elif userInput == '4':
        # export all the data to csv file while new data can be appended but the header remain same

        with open('report.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                                    'Name', 'Difficulty', 'Judges Scores', 'Total Time', 'Final Score'])
            for i in range(len(List)):
                writer.writerow({"Name": List[i][0], "Difficulty": dificultyBigStore[i],
                                "Judges Scores": judgeScore[i], "Total Time": record[i][0], "Final Score": record[i][1]})

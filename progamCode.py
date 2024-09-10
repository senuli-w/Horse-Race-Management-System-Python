import random
from tabulate import tabulate

def horseIdValidation(prompt, horseList):
    while True:
        horseID = input(prompt)
        idAlreadyInUse = 0

        try:
            horseID = int(horseID)
        except:
            # Error occurring means the input is not an integer
            print("Enter a valid Horse ID.")
            continue
            # To ask for another ID

        # Checking if the ID is already registered
        for i in horseList:
            if i["horseID"] == horseID:
                idAlreadyInUse += 1
        
        if idAlreadyInUse >= 1:
            print("Horse ID already in use.")
            print("Enter a new Horse ID.")
            continue
            # To ask for another ID
        else:
            break
    return horseID

def horseGroupValidation(prompt, horseList):
    print("Choose a group from (A, B, C, D)")

    while True:
        group = input(prompt)
        group = group.upper()

        if group not in ("A", "B", "C", "D"):
            print("Enter a Valid group.")
            continue

        # Count the number of horses from the same group
        sameGroupCount = 0
        for i in horseList:
            if i["group"] == group:
                sameGroupCount += 1

        if sameGroupCount >= 5:
            print("No more allocations for the group.")
            print("Enter another group.")
        else:
            break
    return group

def nonEmptyInput(prompt):
    while True:
        userInput = input(prompt).capitalize()

        if userInput.strip() == "":
            print("Enter a valid input.")
        else:
            break
    return userInput

def integerInput(prompt):
    while True:
        userInput = input(prompt)

        try:
            userInput = int(userInput)
            break
        except ValueError:
            print("Enter an integer.")
    return userInput

def addHD(horseList):
    horse = {}
    horse["horseID"] = horseIdValidation("Horse ID : ", horseList)    
    horse["horseName"] = nonEmptyInput("Horse Name : ")
    horse["jockeyName"] = nonEmptyInput("Jockey Name : ")
    horse["age"] = nonEmptyInput("Age : ")
    horse["breed"] = nonEmptyInput("Breed : ")
    horse["raceRecord"] = nonEmptyInput("Race Record : ")
    horse["group"] = horseGroupValidation("Group : ", horseList)

    # Returning the single horse to add to the horseList in the main program.
    return horse

def deleteHD(horseList):
    search = integerInput("Search using the horse ID : ")

    for horse in horseList:
        if horse["horseID"] == search:
            indexOfHorse = horseList.index(horse)
            horseList.pop(indexOfHorse)
            print("Horse", search, "deleted.")
    
    if indexOfHorse == None:
        print("Invalid Horse ID")

    print()
    # Returning horseList to update the horseList in the main program.
    return horseList

def updateHD(horseList):
    indexOfHorse = None
    updateError = False
    search = integerInput("Search using the horse ID : ")

    for horse in horseList:
        if horse["horseID"] == search:
            print("\n(0)\tHorseID\n(1)\tHorse Name\n(2)\tJockey Name\n(3)\tAge\n(4)\tBreed\n(5)\tRace Record\n(6)\tGroup")
            updateNo = integerInput("\nWhat do you want to update?\nEnter the number (0-6) : ")

            if updateNo == 0:
                horse["horseID"] = horseIdValidation("Enter the new Horse ID : ", horseList)
            elif updateNo == 1:
                horse["horseName"] = nonEmptyInput("Enter the new Horse Name : ")
            elif updateNo == 2:
                horse["jockeyName"] = nonEmptyInput("Enter the new Jockey Name : ")
            elif updateNo == 3:
                horse["age"] = nonEmptyInput("Enter the new Age : ")
            elif updateNo == 4:
                horse["breed"] = nonEmptyInput("Enter the new Breed : ")
            elif updateNo == 5:
                horse["raceRecord"] = nonEmptyInput("Enter the new Race Record : ")
            elif updateNo == 6:
                horse["group"] = horseGroupValidation("Enter the new Group : ", horseList)
            else:
                print("Invalid input.")
                updateError = True

            indexOfHorse = True

    if indexOfHorse == None:
        print("Invalid Horse ID")
    elif updateError == True:
        print("Couldn't update!")
    else:
        print("Horse", search, "updated.")
    print("---------------------------------")

    # Returning horseList to update the horselist in the main program.
    return horseList

def viewHD(horseList):
    allHorses = []

    # # Changing the type of horse IDs to int 
    # for i in range(len(horseList)):
    #     horseList[i]["horseID"] = int(horseList[i]["horseID"])
    
    for i in range(len(horseList) - 1):
        # Changing the order of the horses according to ascending order
        for j in range(len(horseList) - 1):
            if horseList[j]["horseID"] > horseList[j + 1]["horseID"]:
                # Swapping larger value with smaller value
                horseList[j], horseList[j + 1] = horseList[j + 1], horseList[j] 
    
    # Getting the values in the list of dictioneries into a list
    for i in horseList: 
        oneHorse = list(i.values())
        allHorses.append(oneHorse)

    # Inserting the headings
    allHorses.insert(0, ["Horse ID", "Horse Name", "Jockey Name", "Age", "Breed", "Race Record", "Group" ])

    table = tabulate(allHorses, headers="firstrow", tablefmt="simple_outline")
    print(table)

    # Returning horseList to update the horselist in the main program.
    return horseList

def saveHD(horseList):
    horseDetailTxtFile = open("HorseDetails.txt", "w")

    groupA = []
    groupB = []
    groupC = []
    groupD = []

    # Seperating the horses according to the groups
    for horse in horseList:
        if horse["group"] == "A":
            groupA.append(horse)
        elif horse["group"] == "B":
            groupB.append(horse)
        elif horse["group"] == "C":
            groupC.append(horse)
        elif horse["group"] == "D":
            groupD.append(horse)

    newHorseList = groupA + groupB + groupC + groupD
    # The horses will be saved in the text file according to the order of the groups.
    # First 5 horses - group A, next five horses - group B, etc.

    # Writing the horses in the text file
    for horse in newHorseList:
        for data in horse.values():
            horseDetailTxtFile.write(str(data) + "\n")
        
        # New line after each horse for seperation
        horseDetailTxtFile.write("\n")
        
    horseDetailTxtFile.close()
    print("Successfully saved data in a text file\n")

def selectRandomly():
    try:
        # Getting the horse data from the text file and saving them in a list of dictioneries
        horseDetailTxtFile = open("horseDetails.txt")
        textData = horseDetailTxtFile.readlines()
        horseDetailTxtFile.close()
    
        # Removing the blank lines in the text file
        for line in textData:
            if line == "\n":
                textData.remove(line)
        
        # Getting the no. of horses saved in the text file
        horseCount = len(textData) // 7

        # To help with in looping
        horseKeys = ["horseID", "horseName", "jockeyName", "age", "breed", "raceRecord", "group"]
        newHorseList = []

        for i in range(horseCount):
            horse = {}
            for j in range(7):
                horse[horseKeys[j]] = textData[7 * i + j][:-1]
            newHorseList.append(horse)

        # Seperating the horses according to the groups
        groupA = []
        groupB = []
        groupC = []
        groupD = []

        for horse in newHorseList:
            if horse["group"] == "A":
                groupA.append(horse)
            elif horse["group"] == "B":
                groupB.append(horse)
            elif horse["group"] == "C":
                groupC.append(horse)
            elif horse["group"] == "D":
                groupD.append(horse)


        # Selecting horses
        # Here, these variables contain dictioneries
        groupAHorse = random.choice(groupA)
        groupBHorse = random.choice(groupB)
        groupCHorse = random.choice(groupC)
        groupDHorse = random.choice(groupD)

        # Printing the selected horses
        print("Horses Selected for the final round\n")
        
        groups = ["Group A", "Group B", "Group C", "Group D"]
        selectedHorses = [groupAHorse, groupBHorse, groupCHorse, groupDHorse]
        
        finalGroups = []

        # Putting the data that need to be printed in a list
        for i in range(4):
            group = [groups[i], selectedHorses[i]["horseID"], selectedHorses[i]["horseName"], selectedHorses[i]["jockeyName"]]
            finalGroups.append(group)

        # Table Headings
        finalGroups.insert(0, ["Group", "Horse ID", "Horse Name", "Jockey Name"])
        print(tabulate(finalGroups, headers="firstrow", tablefmt="rounded_grid" ))
    
        return [groupAHorse, groupBHorse, groupCHorse, groupDHorse]
    except:
        print("No data is saved. Enter 'SHD' to save the data.")
        return []

         # Errors that could occur here
        
        # No existing text file
        # Data is last saved before entering 20 horses (not updated)

def winningHD(finalRound):
    groupOrderTimings = [] # To contain timings in the order of the groups A, B, C, D
    timeValues = [] # To contain the same timings in the ascending order
    timingRange = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    while True:
        randomNumber = random.choice(timingRange)

        # To make sure same timing is not given to many horses
        if randomNumber not in groupOrderTimings:
            groupOrderTimings.append(randomNumber)
            timeValues.append(randomNumber)

            # Only 4 random values are needed
            if len(groupOrderTimings) == 4:
                break

    # Sorting to get them in the first, second, third and fourth order
    timeValues.sort()

    # index of the groupOrderTimings value that matches the element in the timeValues
    firstPlace = finalRound[groupOrderTimings.index(timeValues[0])]   
    secondPlace = finalRound[groupOrderTimings.index(timeValues[1])]
    thirdPlace = finalRound[groupOrderTimings.index(timeValues[2])]

    print("\nWinners of the race")

    # Putting the data that need to be printed in a list
    winList = []
    winList.append(["First Place:", firstPlace['horseName'], f"ID : {firstPlace['horseID']}", f"Timing : {timeValues[0]}s"])
    winList.append(["Second Place:", secondPlace['horseName'], f"ID : {secondPlace['horseID']}", f"Timing : {timeValues[1]}s"])
    winList.append(["Third Place:", thirdPlace['horseName'], f"ID : {thirdPlace['horseID']}", f"Timing : {timeValues[2]}s"])

    print(tabulate(winList, tablefmt="rounded_grid"))
    print()
    
    # Adding the timings to the dictioneries
    firstPlace["timing"] = timeValues[0]
    secondPlace["timing"] = timeValues[1]
    thirdPlace["timing"] = timeValues[2]

    return [firstPlace, secondPlace, thirdPlace]

def visualizeWinH(winners):
    timing = []
    places = ["1st Place", "2nd Place", "3rd Place"] # To help with looping

    print("Winners of the race!")

    # Putting the data that need to be printed in a list
    winList = []
    for i in range(3):
        timing.append("*" * (winners[i]["timing"] // 10))
        winList.append([winners[i]['horseName'], f"ID : {winners[i]['horseID']}", timing[i], f"{winners[i]['timing']}s", places[i]])


    print(tabulate(winList, tablefmt="rounded_grid"))
    print()

def help(raceStartd):
    if raceStartd == False:
        print("AHD   | Add Horse Details")
        print("DHD   | Delete Horse Details")
        print("UHD   | Update Horse Details")
        print("VHD   | View Horse Details")
        print("SHD   | Save Horse Details")
        print("START | Start the Race")
        print("ESC   | Exit the Program")
    else:
        print("VHD   | View Horse Details")
        print("SHD   | Save Horse Details")
        print("SDD   | Select Horses for the final Round")
        print("WHD   | Display the Winning Horses")
        print("ESC   | End the Program")



# The main program starts here
        
# To clear the data that are already saved in the text file
        
textFile = open("horseDetails.txt", "w")
textFile.write("")
textFile.close()

horses = []
winners = []
finalRound = []
raceStarted = False
sddDone = False
whdDone = False
count = 4

print("\n\n\t\t\t\t  Welcome to Rapid Run!")
print("\t\t----------------------------------------------------------\n")
help(raceStarted)

while True:
    if raceStarted == False:
        print("\nAHD | UHD | DHD | VHD | SHD | START | ESC | HELP")
    else:
        print("\nVHD | SHD | SDD | WHD | VWH | ESC | HELP")


    if len(horses) == count and raceStarted == False:
        print("\nEnter START to start the game.")
        print("Enter SHD to save the data.\n")
        print("Once the game is started, horse details cannot be edited or deleted!")
        print("Update or Delete the horse details before starting the Game!\n")

    userInput = input("\n> ")
    userInput = userInput.upper().strip()

    if userInput == "START":
        if raceStarted == True:
            print("Race Started already!\n")
        elif len(horses) == count:
            print("\n---Race Started---\n")
            raceStarted = True
            # Displaying the commands with descriptions
            help(raceStarted)
        else:
            print("No enough horses!\nRace cannot start yet!")

    elif userInput == "AHD":
        if raceStarted == True:
            print("Race Started already!\n")
        elif len(horses) == count:
            print("Horse limit exceeded!\n")
        else:
            horses.append(addHD(horses))

    elif userInput == "DHD":
        if raceStarted == True:
            print("Race started already!\n")
        else:
            horses = deleteHD(horses)

    elif userInput == "UHD":
        if raceStarted == True:
            print("Race started already!\n")
        else:
            horses = updateHD(horses)

    elif userInput == "VHD":
        horses = viewHD(horses)

    elif userInput == "SHD":
        saveHD(horses)

    elif userInput == "SDD":
        if raceStarted == False:
            print("Race has not started yet!\n")
        elif sddDone == True:
            print("Final Round has started already!\n")
        else:
            finalRound = selectRandomly()
            # Returns an empty list if any error occurs inside the function
            # If no empty list is retured, that means succcessfully completed SDD
            if finalRound != []:
                sddDone = True

    elif userInput == "WHD":
        if finalRound == []:
            print("No horses are selected to the final round.")
            print("Enter SDD to select horses for the final round.")
        elif whdDone == True:
            print("Final Round is over!")
        else:
            winners = winningHD(finalRound)
            whdDone = True

    elif userInput == "VWH":
        if whdDone == False:
            print("No winners yet. Enter WHD to get the winning horses.")
        else:
            visualizeWinH(winners)
            print("Enter ESC to exit the program.")

    elif userInput == "HELP":
        help(raceStarted)
                
    elif userInput == "ESC":
        print("End of the program!")
        break

    else:
        print("Enter a valid command.")

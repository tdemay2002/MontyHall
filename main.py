import random

def randomDoor():
    return random.randint(0,2)

def setupDoors():
    newDoors = [0,0,0]
    correctDoor = randomDoor()
    newDoors[correctDoor] = 1
    return newDoors, correctDoor

def montyHallAlgorithm(switchDoorBool, correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses):
        nonPickedDoor = [0,1,2]
        openedDoor = -1
        nonOpenedDoor = -1

        doors, correctDoor = setupDoors()

        # door is picked
        pickedDoor = randomDoor()
        nonPickedDoor.remove(pickedDoor)

        # empty door is opened! 
        if (nonPickedDoor[0] == correctDoor):
            openedDoor = nonPickedDoor[1]
            nonOpenedDoor = nonPickedDoor[0]
        else:
            openedDoor = nonPickedDoor[0]
            nonOpenedDoor = nonPickedDoor[1]

        # switch doors
        if (switchDoorBool == True):
            pickedDoor = nonOpenedDoor

            if (pickedDoor == correctDoor):
                print("SWITCH: You got it right!")
                correctSwitchingGuesses += 1
            else:
                print("SWITCH: You got it wrong")
                incorrectSwitchingGuesses += 1


        # dont switch
        elif (switchDoorBool == False):

            if (pickedDoor == correctDoor):
                print("STAY: You got it right!")
                correctStayGuesses += 1
            else: 
                print("STAY: You got it wrong")
                incorrectStayGuesses += 1
        
        return correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses


def main():
    correctSwitchingGuesses = 0
    incorrectSwitchingGuesses = 0
    correctStayGuesses = 0
    incorrectStayGuesses = 0

    for _ in range(100):
        correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses = montyHallAlgorithm(True, correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses)
        correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses = montyHallAlgorithm(False, correctSwitchingGuesses, incorrectSwitchingGuesses, correctStayGuesses, incorrectStayGuesses)

    switchProb = (correctSwitchingGuesses/(correctSwitchingGuesses+incorrectSwitchingGuesses))*100
    stayProb = (correctStayGuesses/(correctStayGuesses+incorrectStayGuesses))*100
    print(f"\nCorrect {correctSwitchingGuesses} times.")
    print(f"Incorrect {incorrectSwitchingGuesses} times.")
    print(f"Probability from switching doors is: {switchProb:.2f}%")
    
    print(f"\nCorrect {correctStayGuesses} times.")
    print(f"Incorrect {incorrectStayGuesses} times.")
    print(f"Probability from stay doors is: {stayProb:.2f}%")

if __name__ == "__main__":
    main()
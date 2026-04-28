import random

# change to how many simulations you would like to run
NUM_SIMULATIONS = 10000

switchCase = {
    "correct": 0,
    "incorrect": 0,
    "prob": 0.0
}
stayCase = {
    "correct": 0,
    "incorrect": 0,
    "prob": 0.0
}


def randomDoor():
    return random.randint(0,2)


def calcWinProb(numCorrect, numIncorrect):
    return (numCorrect/(numCorrect+numIncorrect))*100


def montyHallAlgorithm(switchDoorBool):
        nonPickedDoor = [0,1,2]
        nonOpenedDoor = -1

        # there exists 1 correct door
        correctDoor = randomDoor()

        # user picks a door
        pickedDoor = randomDoor()
        nonPickedDoor.remove(pickedDoor)

        # host reveals an empty door! (Get the door that was not opened or picked)
        if (nonPickedDoor[0] == correctDoor):
            nonOpenedDoor = nonPickedDoor[0]
        else:
            nonOpenedDoor = nonPickedDoor[1]

        # does user want to switch to the other closed door?
        # update wins
        if (switchDoorBool):
            pickedDoor = nonOpenedDoor
            
            if (pickedDoor == correctDoor):
                switchCase["correct"] += 1
            else:
                switchCase["incorrect"] += 1

        else:
            if (pickedDoor == correctDoor):
                stayCase["correct"] += 1
            else:
                stayCase["incorrect"] += 1


def runSimulations(switchDoorBool):
    for _ in range(NUM_SIMULATIONS):
        montyHallAlgorithm(switchDoorBool)
    
    if (switchDoorBool):
        switchCase["prob"] = calcWinProb(switchCase["correct"], switchCase["incorrect"])
    else:
        stayCase["prob"] = calcWinProb(stayCase["correct"], stayCase["incorrect"])


def printResults():
    correctSwitchString = f" * Correct {switchCase["correct"]} times. "
    incorrectSwitchString = f" * Incorrect {switchCase["incorrect"]} times. "
    switchProbString = f" * Probability of winning: {switchCase["prob"]:.2f}% "
    correctStayString = f" * Correct {stayCase["correct"]} times. "
    incorrectStayString = f" * Incorrect {stayCase["incorrect"]} times. "
    stayProbString = f" * Probability of winning: {stayCase["prob"]:.2f}% "

    textWidth = max(
        len(correctSwitchString),
        len(incorrectSwitchString),
        len(switchProbString),
        len(correctStayString),
        len(incorrectStayString),
        len(stayProbString)
    )
    print("+" + "-"*textWidth + "-----" + "-"*textWidth + "+")
    print("|" + f"{'MONTY HALL PROBLEM':^{textWidth*2 + 5}}" + "|")
    print("+" + "-"*textWidth + "--+--" + "-"*textWidth + "+")
    print("|" + f"{'SWITCH':^{textWidth}}  |  {'STAY':^{textWidth}}" + "|")
    print("+" + "-"*textWidth + "--+--" + "-"*textWidth + "+")
    print("|" + f"{correctSwitchString:<{textWidth}}  |  {correctStayString:<{textWidth}}" + "|")
    print("|" + f"{incorrectSwitchString:<{textWidth}}  |  {incorrectStayString:<{textWidth}}" + "|")
    print("|" + f"{switchProbString:<{textWidth}}  |  {stayProbString:<{textWidth}}" + "|")
    print("+" + "-"*textWidth + "--+--" + "-"*textWidth + "+")



def main():

    # case when choosing to switch
    switchDoor = True
    runSimulations(switchDoor)

    # case when choosing to stay
    switchDoor = False
    runSimulations(switchDoor)

    printResults()

if __name__ == "__main__":
    main()
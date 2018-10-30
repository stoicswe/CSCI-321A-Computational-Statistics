import numpy as np
import random as rm

# The statespace
states = ["Sleep","Icecream","Run", "Ping-Pong", "COMSCI Study"]

# Possible sequences of events
transitionName = [["SS","SR","SI","SP","SC"],["RS","RR","RI","RP","RC"],["IS","IR","II","IP","IC"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [
    [0.1,0.6,0.09,0.2,0.01],
    [0.1,0.6,0.01,0.2,0.09],
    [0.05,0.2,0.05,0.4,0.3],
    [0.5,0.3,0.025,0.025,0.2],
    [0.03,0.7,0.04,0.15,0.08]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
    print("Somewhere, something went wrong. Transition matrix, perhaps?")
else: print("All is gonna be okay, you should move on!! ;)")

# A function that implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sleep"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.1
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            elif change == "SI":
                prob = prob * 0.09
                activityToday = "Icecream"
                activityList.append("Icecream")
            elif change == "SP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.01
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            # [0.1,0.6,0.01,0.2,0.09],
            if change == "RR":
                prob = prob * 0.1
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.6
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "RI":
                prob = prob * 0.01
                activityToday = "Icecream"
                activityList.append("Icecream")
            elif change == "RP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.09
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.05,0.2,0.05,0.4,0.3],
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "IR":
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
            elif change == "IP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.09
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Ping-Pong":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.5,0.3,0.025,0.025,0.2],
            if change == "PI":
                prob = prob * 0.5
                activityList.append("Icecream")
                pass
            elif change == "PS":
                prob = prob * 0.3
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "PR":
                prob = prob * 0.25
                activityToday = "Run"
                activityList.append("Run")
            elif change == "PP":
                prob = prob * 0.25
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.2
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "COMSCI Study":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.03,0.7,0.04,0.15,0.08]]
            if change == "CI":
                prob = prob * 0.03
                activityList.append("Icecream")
                pass
            elif change == "CS":
                prob = prob * 0.7
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "CR":
                prob = prob * 0.04
                activityToday = "Run"
                activityList.append("Run")
            elif change == "CP":
                prob = prob * 0.15
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.08
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        i += 1   
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)

def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sleep"
    activityList = [activityToday]
    i = 0
    prob = 1
    while i != days:
        if activityToday == "Sleep":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.1
                activityList.append("Sleep")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Run"
                activityList.append("Run")
            elif change == "SI":
                prob = prob * 0.09
                activityToday = "Icecream"
                activityList.append("Icecream")
            elif change == "SP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.01
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Run":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            # [0.1,0.6,0.01,0.2,0.09],
            if change == "RR":
                prob = prob * 0.1
                activityList.append("Run")
                pass
            elif change == "RS":
                prob = prob * 0.6
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "RI":
                prob = prob * 0.01
                activityToday = "Icecream"
                activityList.append("Icecream")
            elif change == "RP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.09
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Icecream":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.05,0.2,0.05,0.4,0.3],
            if change == "II":
                prob = prob * 0.1
                activityList.append("Icecream")
                pass
            elif change == "IS":
                prob = prob * 0.2
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "IR":
                prob = prob * 0.7
                activityToday = "Run"
                activityList.append("Run")
            elif change == "IP":
                prob = prob * 0.2
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.09
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "Ping-Pong":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.5,0.3,0.025,0.025,0.2],
            if change == "PI":
                prob = prob * 0.5
                activityList.append("Icecream")
                pass
            elif change == "PS":
                prob = prob * 0.3
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "PR":
                prob = prob * 0.25
                activityToday = "Run"
                activityList.append("Run")
            elif change == "PP":
                prob = prob * 0.25
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.2
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        elif activityToday == "COMSCI Study":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            # [0.03,0.7,0.04,0.15,0.08]]
            if change == "CI":
                prob = prob * 0.03
                activityList.append("Icecream")
                pass
            elif change == "CS":
                prob = prob * 0.7
                activityToday = "Sleep"
                activityList.append("Sleep")
            elif change == "CR":
                prob = prob * 0.04
                activityToday = "Run"
                activityList.append("Run")
            elif change == "CP":
                prob = prob * 0.15
                activityToday = "Ping-Pong"
                activityList.append("Ping-Pong")
            else:
                prob = prob * 0.08
                activityToday = "COMSCI Study"
                activityList.append("COMSCI Study")
        i += 1    
    return activityList

# To save every activityList
list_activity = []
count = 0

# `Range` starts from the first count up until but excluding the last count
for iterations in range(1,10000):
        list_activity.append(activity_forecast(2))

# Check out all the `activityList` we collected    
#print(list_activity)

# Iterate through the list to get a count of all activities ending in state:'Run'
for smaller_list in list_activity:
    if(smaller_list[2] == "Run"):
        count += 1

# Calculate the probability of starting from state:'Sleep' and ending at state:'Run'
percentage = (count/10000) * 100
print("The probability of starting at state:'Sleep' and ending at state:'Run'= " + str(percentage) + "%")

